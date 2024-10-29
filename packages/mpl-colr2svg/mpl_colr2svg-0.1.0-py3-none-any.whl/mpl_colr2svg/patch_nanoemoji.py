# We use nanoemoji to convert colr to svg. However, we patch two function.

# 1. svgPathPen in nanoemoji seems to have a bug in qCurveTo when there is None at the end.
# We patch nanoemoji to use fontTools.pens.svgPathPen instead.

# 2. 
# original glyph_region seems not properly set the glyph viewBox. For version >
# 4, which is True for segoe fonts, we use usWindAscent and etc.


import nanoemoji.colr_to_svg

from fontTools.pens.transformPen import TransformPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from picosvg.geometric_types import Rect


def _draw_svg_path(
    svg_path,
    glyph_set,
    glyph_name,
    font_to_vbox,
):
    # use glyph set to resolve references in composite glyphs
    svg_pen = SVGPathPen(glyph_set)
    # wrap svg pen with "filter" pen mapping coordinates from UPEM to SVG space
    transform_pen = TransformPen(svg_pen, font_to_vbox)

    glyph = glyph_set[glyph_name]
    glyph.draw(transform_pen)

    svg_path.attrib["d"] = svg_pen.getCommands()


def glyph_region(ttfont: TTFont, glyph_name: str) -> Rect:
    """The area occupied by the glyph, NOT factoring in that Y flips.

    map_font_space_to_viewbox handles font +y goes up => svg +y goes down."""
    width = ttfont["hmtx"][glyph_name][0]

    if ttfont["OS/2"].version >= 4:
        ascender = ttfont["OS/2"].usWinAscent
        descender = -ttfont["OS/2"].usWinDescent
    else:
        ascender = ttfont["OS/2"].sTypoAscender
        descender = ttfont["OS/2"].sTypoDescender

    return Rect(
        0,
        -ascender,
        width,
        ascender - descender,
    )

def monkey_patch_nanoemoji():
    if nanoemoji.colr_to_svg._draw_svg_path is not _draw_svg_path:
        nanoemoji.colr_to_svg._draw_svg_path = _draw_svg_path
        nanoemoji.colr_to_svg.glyph_region = glyph_region
