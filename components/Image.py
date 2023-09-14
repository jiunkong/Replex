from __future__ import annotations

from typing import Optional, final, overload

import pygame

from .Base import InteractiveComponent
from ..utils.position import float2d, int2d
from ..utils.color import Color
from ..utils.font import getFont, Font

__all__ = ['Image']

class Image(InteractiveComponent):
    @overload
    def __init__(self, pos: float2d, path: str):
        ...
    
    @overload
    def __init__(self, pos: float2d, pygameSurface: pygame.surface.Surface):
        ...

    def __init__(self, pos: float2d, value: str | pygame.surface.Surface) -> None:
        if isinstance(value, pygame.surface.Surface):
            self.__image = value
        elif isinstance(value, str):
            self.__image: pygame.surface.Surface = pygame.image.load(value)
        else:
            raise Exception("Image source must not be None")
            
        super().__init__(pos, self.__image.get_size())

    @final
    def getPygameImage(self) -> pygame.surface.Surface:
        return self.__image

    @final
    def rescale(self, size: int2d) -> Image:
        self.__image = pygame.transform.scale(self.__image, size)
        self.size = size
        return self
    
    @staticmethod
    def textToImageByFont(text: str, font: Font, color: Color, antialias: bool = True) -> Image:
        image = font.render(text, antialias, color.rgba)
        return Image(_pygameSurface=image)

    @staticmethod
    def textToImageByFontName(text: str, fontName: str, color: Color, antialias: bool = True) -> Optional[Image]:
        font = getFont(fontName)
        return Image.textToImageByFont(text, font, color, antialias) if font is not None else None

'''class DynamicImage(Image, DynamicObject):
    def __init__(self, path: Optional[str] = None, pos: Pos = (0, 0), image: Optional[Image] = None, _pygameSurface: Optional[pygame.surface.Surface] = None) -> None:

        #if image or _pygameSurface is given, Image is generated by using it.

        if not image is None:
            _pygameSurface = image.getPygameImage()

        super().__init__(path, pos, _pygameSurface)

    def getPygameSurface(self) -> pygame.surface.Surface:
        return self.getPygameImage()'''