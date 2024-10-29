import numpy as np
from matplotlib import rcParams
from matplotlib.offsetbox import AnnotationBbox
from mpl_simple_svg_parser import SVGMplPathIterator
from . import Colr2SVG

from abc import ABC, abstractmethod


class ColorEmojiBase(ABC):
    @abstractmethod
    def _get_svg(self, c: str, size: int) -> bytes:
        ...

    def get_svg_mpl_path_iterator(self, c, size=128):
        """
        c: unicode character
        size: size of returned svg object. While it is a vector format, the size matter
              as we rasterize gradients as images.
        """

        b_xmlstring = self._get_svg(c, size)

        svg_mpl_path_iterator = SVGMplPathIterator(b_xmlstring)

        return svg_mpl_path_iterator

    def get_drawing_area(self, ax, c, wmax=np.inf, hmax=np.inf, gradient_image_size=128):
        smpi = self.get_svg_mpl_path_iterator(c, size=gradient_image_size)
        return smpi.get_drawing_area(ax, wmax=wmax, hmax=hmax)

    def draw(self, ax, c, size=128):
        smpi = self.get_svg_mpl_path_iterator(c, size=size)
        return smpi.draw(ax)


    def annotate(self, ax, c, *kl, emoji_scale=1.5, gradient_image_size=128, **kwargs):
        if "frameon" not in kwargs:
            kwargs["frameon"] = False
        hmax = kwargs.pop("fontsize", rcParams["font.size"]) * emoji_scale
        da = self.get_drawing_area(ax, c, hmax=hmax, gradient_image_size=gradient_image_size)
        ann = AnnotationBbox(da, *kl, **kwargs)
        ax.add_artist(ann)

        return ann


class ColorEmoji(ColorEmojiBase):
    def __init__(self, ftname):
        self._colr2svg = Colr2SVG(ftname)

    def _get_svg(self, c: str, size: int) -> bytes:
        svg_el = self._colr2svg.get(c)

        etree = Colr2SVG.get_scaled_svg(svg_el, size)
        b_xmlstring = Colr2SVG.tostring(etree)

        return b_xmlstring

    # def get_svg_mpl_path_iterator(self, c, size=128):
    #     """
    #     c: unicode character
    #     size: size of returned svg object. While it is a vector format, the size matter
    #           as we rasterize gradients as images.
    #     """
    #     svg_el = self._colr2svg.get(c)

    #     etree = Colr2SVG.get_scaled_svg(svg_el, size)
    #     b_xmlstring = Colr2SVG.tostring(etree)

    #     svg_mpl_path_iterator = SVGMplPathIterator(b_xmlstring)

    #     return svg_mpl_path_iterator

