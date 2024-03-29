from abc import ABCMeta, abstractmethod

from .Surface import Surface
from .Base import int2d
from ..utils.language import Language

__all__ = ['Scene']

class Scene(Surface, metaclass=ABCMeta):
    def __init__(self, size: int2d) -> None:
        super().__init__((0, 0), size)

    def onEnterScene(self) -> None:
        pass

    def onEscapeScene(self) -> None:
        Language.clearEventListeners()

    @abstractmethod
    def draw(self):
        pass

    def tick(self):
        super().tick()
