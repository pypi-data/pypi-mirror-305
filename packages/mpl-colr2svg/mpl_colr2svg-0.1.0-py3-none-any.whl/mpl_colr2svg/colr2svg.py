"""Extract svg from the COLR tabel of the font. Under the hood, nanoemoji's
colr_to_svg module is used for the conversion.

"""

# FIXME: check if black-renderer can be better than nanoemoji. While not
# directly related, if a support for variable font is required, we may use
# blackrender.

# black-renderer : https://github.com/BlackFoundryCom/black-renderer
# nanoemoji : https://github.com/googlefonts/nanoemoji


from fontTools.ttLib import TTFont

from .patch_nanoemoji import monkey_patch_nanoemoji

monkey_patch_nanoemoji()

from nanoemoji.colr_to_svg import glyph_region
from nanoemoji.colr_to_svg import (_colr_v0_glyph_to_svg,
                                   _colr_v1_glyph_to_svg)

from lxml import etree
from copy import copy


class Ligatures:
    def __init__(self, gsub, cmap):
        # only select LookupType of 4, which are ligatures. FIXME Not sure if
        # updating the dictionary in sequence is a right approch.
        self._cmap = cmap
        self._ligatures = dict()
        for lookup in gsub.table.LookupList.Lookup:
            if lookup.LookupType == 4:
                for tbl in lookup.SubTable:
                    for g, l in tbl.ligatures.items():
                        k = self._ligatures.setdefault(g, [])
                        k.extend(l)

    def get_gid(self, c):
        # check the ligature mapping to find a glyph id. Return None if not found.
        gidl = list(self._cmap[ord(c1)] for c1 in c)

        t = self._ligatures.get(gidl[0], None)
        if t is None:
            return None
        kk = dict([(tuple(t1.Component), t1) for t1 in t])
        lig = kk.get(tuple(gidl[1:]), None)
        if lig is None:
            return None

        return lig.LigGlyph


class Colr2SVG:
    """Extract SVG element of glyphs from the COLR table."""
    def __init__(self, ftname, view_box_callback=None):
        self._font = TTFont(ftname, lazy=True)

        assert "COLR" in self._font

        self._colr_version = self._font["COLR"].version

        self._cmap = self._font["cmap"].getBestCmap() # tables[4]
        self._glyph_set = self._font.getGlyphSet()
        self._view_box_callback = self._view_box if view_box_callback is None else view_box_callback
        if self._colr_version == 0:
            self._colr_glyph_to_svg = _colr_v0_glyph_to_svg
            self._glyph_map = dict((g, g) for g in self._font["COLR"].ColorLayers)

        elif self._colr_version == 1:
            self._colr_glyph_to_svg = _colr_v1_glyph_to_svg
            _glyph_list = self._font["COLR"].table.BaseGlyphList.BaseGlyphPaintRecord
            self._glyph_map = dict((g.BaseGlyph, _glyph_list[i] ) for i, g in
                                   enumerate(_glyph_list))

        gsub = self._font["GSUB"]
        self._ligatures = Ligatures(gsub, self._cmap)

    def get(self, c):
        # if the second character is a Variation Selector, we simply drop it.
        # This seems to work for characters like ❤️, but not sure if this is a
        # general solution.
        if len(c) == 2 and c[1] == "️":
            c = c[0]

        if len(c) == 1:
            gid = self._cmap[ord(c)]
        else:
            gid = self._ligatures.get_gid(c)

        g = self._glyph_map[gid]

        svg_el = self._colr_glyph_to_svg(self._font, self._glyph_set,
                                         self._view_box_callback,
                                         g)

        return svg_el

    def _view_box(self, glyph_name: str):
        # we want a viewbox that results in no scaling when translating from font-space

        return glyph_region(self._font, glyph_name)

    # svg helper
    @staticmethod
    def tostring(svg_el):
        return etree.tostring(svg_el)

    @staticmethod
    def get_scaled_svg(svg_el, size):
        svg_el = copy(svg_el)
        xywh = svg_el.attrib["viewBox"].split()
        x, y, w, h = map(float, xywh)
        scale = min(size / w, size / h)
        svg_el.attrib["viewBox"] = f"{x*scale} {y*scale} {w*scale} {h*scale}"

        paths = svg_el[1:]
        svg_el[1:] = [etree.Element("g")]
        svg_el[1][:] = paths

        svg_el[1].attrib["transform"] = f"translate({x*scale} {y*scale}) scale({scale} {scale}) translate({-x} {-y}) "

        return svg_el
