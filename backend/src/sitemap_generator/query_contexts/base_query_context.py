from abc import ABC, abstractmethod
from typing import TypeVar


class AbstractQueryContext(ABC):
    @abstractmethod
    def filter_expressions(self) -> list:
        raise NotImplementedError


QueryContext = TypeVar('QueryContext', bound=AbstractQueryContext)
