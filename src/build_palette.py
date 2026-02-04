#!/usr/bin/env python3

# ruff: noqa: E741

import argparse
import math
import re
import subprocess
from configparser import ConfigParser, SectionProxy
from dataclasses import dataclass
from string import Template
from typing import Any, Generator, Literal, TypeAlias


def cbrt(i: float) -> float:
    return math.pow(i, 1 / 3)


# Ported from <https://github.com/Qix-/color-convert/blob/07e073af02e9a3722f6926d214ffd778af20ab03/conversions.js>
class ColorConvert:
    @staticmethod
    def srgb_nonlinear_transform(c: float) -> float:
        c = ((1.055 * (c ** (1 / 2.4))) - 0.055) if c > 0.003_130_8 else (c * 12.92)
        return min(max(0, c), 1)

    @staticmethod
    def srgb_nonlinear_transform_invert(c: float) -> float:
        return (((c + 0.055) / 1.055) ** 2.4) if c > 0.040_45 else (c / 12.92)

    @staticmethod
    def rgb2oklab(r: float, g: float, b: float) -> tuple[float, float, float]:
        # Assume sRGB
        r = ColorConvert.srgb_nonlinear_transform_invert(r / 255)
        g = ColorConvert.srgb_nonlinear_transform_invert(g / 255)
        b = ColorConvert.srgb_nonlinear_transform_invert(b / 255)

        lp = cbrt(0.412_221_470_8 * r + 0.536_332_536_3 * g + 0.051_445_992_9 * b)
        mp = cbrt(0.211_903_498_2 * r + 0.680_699_545_1 * g + 0.107_396_956_6 * b)
        sp = cbrt(0.088_302_461_9 * r + 0.281_718_837_6 * g + 0.629_978_700_5 * b)

        l = 0.210_454_255_3 * lp + 0.793_617_785 * mp - 0.004_072_046_8 * sp
        a = 1.977_998_495_1 * lp - 2.428_592_205 * mp + 0.450_593_709_9 * sp
        b = 0.025_904_037_1 * lp + 0.782_771_766_2 * mp - 0.808_675_766 * sp

        return l * 100, a * 100, b * 100

    @staticmethod
    def oklab2rgb(l: float, a: float, b: float) -> tuple[float, float, float]:
        l = l / 100
        a = a / 100
        b = b / 100

        lp = (l + 0.396_337_777_4 * a + 0.215_803_757_3 * b) ** 3
        mp = (l - 0.105_561_345_8 * a - 0.063_854_172_8 * b) ** 3
        sp = (l - 0.089_484_177_5 * a - 1.291_485_548 * b) ** 3

        r = (4.076_741_662_1 * lp) - (3.307_711_591_3 * mp) + (0.230_969_929_2 * sp)
        g = (-1.268_438_004_6 * lp) + (2.609_757_401_1 * mp) - (0.341_319_396_5 * sp)
        b = (-0.004_196_086_3 * lp) - (0.703_418_614_7 * mp) + (1.707_614_701 * sp)

        # Assume sRGB
        r = ColorConvert.srgb_nonlinear_transform(r)
        g = ColorConvert.srgb_nonlinear_transform(g)
        b = ColorConvert.srgb_nonlinear_transform(b)

        return r * 255, g * 255, b * 255

    @staticmethod
    def hex2rgb(hex: str) -> tuple[float, float, float]:
        if len(hex) == 3:
            i = int(hex, 16)
            r = (i >> 8) & 0xF
            g = (i >> 4) & 0xF
            b = (i >> 0) & 0xF
            r |= r << 4
            g |= g << 4
            b |= b << 4
        elif len(hex) == 6:
            i = int(hex, 16)
            r = (i >> 16) & 0xFF
            g = (i >> 8) & 0xFF
            b = (i >> 0) & 0xFF
        else:
            raise ValueError(f"'{hex}' is not a valid hex color")

        return float(r), float(g), float(b)

    @staticmethod
    def rgb2hex(r: float, g: float, b: float) -> str:
        return f"{round(r):02x}{round(g):02x}{round(b):02x}"


Palette: TypeAlias = dict[str, str | None]


@dataclass
class Config:
    dark: Palette
    light: Palette
    current: Palette | None


@dataclass
class Token:
    type: Literal["str", "usepalette", "endpalette"]
    data: str
    line: str


PALETTE_COLORS = [f"base{i:02X}" for i in range(0, 16)]
BLOCK_PATTERN = re.compile(r"%(?P<key>usepalette|endpalette) (?P<val>[a-zA-Z_-]+)$")


def brighten(hex: str, d: str) -> str:
    r, g, b = ColorConvert.hex2rgb(hex)
    l, a, b = ColorConvert.rgb2oklab(r, g, b)

    p = d.rstrip("%")
    if p == d:
        l += float(p)
    else:
        l += l * float(p) / 100

    r, g, b = ColorConvert.oklab2rgb(l, a, b)
    return ColorConvert.rgb2hex(r, g, b)


def tmux_format(format: str) -> str:
    res = subprocess.run(
        ["tmux", "display-message", "-p", format],
        capture_output=True,
        text=True,
        check=True,
    )
    return res.stdout.strip()


def parse_palette(parser: SectionProxy) -> Palette:
    palette = dict()

    for k in ["scheme", "author"]:
        v = parser.get(k)
        if v is None:
            raise KeyError(f'missing required property "{k}"')
        palette[k] = v

    for k in ["bright", "dim"]:
        palette[k] = parser.get(k)

    for k in PALETTE_COLORS:
        v = parser.get(k)
        if v is None:
            raise KeyError(f'missing palette color "{k}"')
        palette[k] = v.lstrip("#")

    return palette


def parse_config(parser: ConfigParser) -> Config:
    config: dict[str, Any] = dict(current=None)

    for k in ["dark", "light"]:
        if not parser.has_section(k):
            raise KeyError(f'missing palette "{k}"')
        config[k] = parse_palette(parser[k])

    return Config(**config)


def tokenize_template(template: str) -> Generator[Token, None, None]:
    for line in template.splitlines(keepends=True):
        mat = BLOCK_PATTERN.search(line)
        if mat is not None:
            yield Token(type=mat[1], data=mat[2], line=line)  # type: ignore
        else:
            yield Token(type="str", data=line, line=line)


def render_template(config: Config, template: str) -> str:
    @dataclass
    class Context:
        block: str
        palette: Palette | None

    context: list[Context] = list()
    res: list[str] = list()
    for tok in tokenize_template(template):
        match tok.type:
            # instruction: %usepalette {palette}-{variant}
            case "usepalette":
                key, variant, *_ = tok.data.split("-") + [None]
                if key is None or key == "":
                    raise ValueError(f"missing palette identifier: {tok.line.strip()}")

                palette: Palette | None = getattr(config, key, None)
                if palette is None:
                    raise KeyError(f'missing palette "{key}"')

                if palette is None or variant is None:
                    pass
                elif palette.get(variant) is None:
                    palette = None
                else:
                    palette, d = palette.copy(), palette[variant]
                    for k in PALETTE_COLORS:
                        palette[k] = brighten(palette[k], d)  # type: ignore

                context.append(Context(tok.data, palette))

            # instruction: %endpalette
            case "endpalette":
                if len(context) == 0 or tok.data != context[-1].block:
                    raise ValueError(f"unmatched block terminator: f{tok.line.strip()}")
                context.pop()

            case "str":
                if len(context) == 0:
                    res.append(tok.data)
                elif context[-1].palette is None:
                    pass  # skip block if palette not provided
                else:
                    res.append(Template(tok.data).substitute(context[-1].palette))

    return "".join(res)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config",
        help="path to palette configuration",
    )
    parser.add_argument(
        "--current",
        help="palette variant currently in use",
    )
    parser.add_argument(
        "-i",
        "--input",
        required=True,
        help="path to input template",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="path to write output",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if args.config is None:
        args.config = tmux_format("#{@base16-palettes}/gruvbox-material.ini")
    if args.current is None:
        args.current = tmux_format("#{@base16-background}")

    with open(args.config, "r") as f:
        parser = ConfigParser(interpolation=None)
        parser.read_file(f)
        config = parse_config(parser)
    config.current = getattr(config, args.current)

    with open(args.input, "r") as f:
        input = f.read()

    output = render_template(config, input)
    if args.output is not None:
        with open(args.output, "w") as f:
            f.write(output)
    else:
        print(output)


if __name__ == "__main__":
    main()
