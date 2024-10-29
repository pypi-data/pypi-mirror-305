"""
ColorEmojiBlackrenderer: uses blackrenderer package to render color emoji to svg.
"""

# from typing import NamedTuple
from io import BytesIO

from blackrenderer.font import BlackRendererFont
from blackrenderer.render import (buildGlyphLine, calcGlyphLineBounds)
from blackrenderer.backends.cairo import CairoSVGSurface

from fontTools.misc.arrayTools import (
    scaleRect,
    intRect,
    insetRect,
)
import uharfbuzz as hb

from .color_emoji import ColorEmojiBase


class ColorEmojiBlackrenderer(ColorEmojiBase):
    def __init__(self, fontPath):
        self._font = BlackRendererFont(fontPath)
        self._glyphNames = self._font.glyphNames

    def get_svg(self,
                textString,
                fontSize,
                margin=None,
                features=None,
                variations=None,
                paletteIndex=0,
                backendName=None,
                lang=None,
                script=None) -> bytes:

        if margin is None:
            margin = int(fontSize * 0.08)

        font = self._font

        scaleFactor = fontSize / font.unitsPerEm

        buf = hb.Buffer()
        buf.add_str(textString)
        buf.guess_segment_properties()

        if script:
            buf.script = script
        if lang:
            buf.language = lang
        if variations:
            font.setLocation(variations)
        palette = font.getPalette(paletteIndex)

        hb.shape(font.hbFont, buf, features)

        infos = buf.glyph_infos
        positions = buf.glyph_positions
        glyphLine = buildGlyphLine(infos, positions, self._glyphNames)
        bounds = calcGlyphLineBounds(glyphLine, font)
        bounds = scaleRect(bounds, scaleFactor, scaleFactor)
        bounds = insetRect(bounds, -margin, -margin)
        bounds = intRect(bounds)

        # the SVG gradient created by backrenderer's SVGSurface or
        # SkiaSVGSurface is somehow not correctly rendered by cairosvg. On the other
        # hand, CairoSVGSurface works okay.

        surface = CairoSVGSurface()
        with surface.canvas(bounds) as canvas:
            canvas.scale(scaleFactor)
            for glyph in glyphLine:
                with canvas.savedState():
                    canvas.translate(glyph.xOffset, glyph.yOffset)
                    font.drawGlyph(glyph.name, canvas, palette=palette)
                canvas.translate(glyph.xAdvance, glyph.yAdvance)

        b = BytesIO()
        surface.saveImage(b)
        b_xmlstring = b.getvalue()

        return b_xmlstring

    def _get_svg(self, c, size=128):
        return self.get_svg(c, size)
