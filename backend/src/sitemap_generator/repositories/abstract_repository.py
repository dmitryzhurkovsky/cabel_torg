from abc import ABC, abstractmethod
from typing import TypeVar


class AbstractRepository(ABC):
    @abstractmethod
    def get_all_records(self):
        raise NotImplementedError


Repository = TypeVar('Repository', bound=AbstractRepository)
