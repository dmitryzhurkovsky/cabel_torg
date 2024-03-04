from abc import ABC, abstractmethod
from typing import TypeVar


class AbstractFileManager(ABC):
    @abstractmethod
    def write(self, data):
        raise NotImplementedError


FileManager = TypeVar('FileManager', bound=AbstractFileManager)
