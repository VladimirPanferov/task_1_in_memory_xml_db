from abc import ABC, abstractmethod
from typing import (
    List,
    Dict,
)

class BaseFile(ABC):

    @abstractmethod
    def info(self) -> dict:
        pass


class XMLFile(BaseFile):
    import xml

    def __init__(self, data: str) -> None:
        super().__init__()
        # self._data = data


class xMLDB:

    def __init__(self) -> None:
        self.files = {}

    def info(self) -> List[Dict]:
        result = []
        for key, value in self.files.items():
            result.append({key, value.info()})
        return result

    def add(self, key: str, value: str) -> None:
        pass

    def stats(self) -> dict:
        pass

    def _validate_file(self, value: str) -> bool:
        pass
