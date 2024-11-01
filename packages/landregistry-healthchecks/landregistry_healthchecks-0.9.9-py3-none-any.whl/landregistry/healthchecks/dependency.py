from enum import Enum
from typing import Any, Callable, Optional


class DependencyType(Enum):
    WEB = 1
    DB = 2
    OTHER = 3


class Dependency(object):
    def __init__(
        self,
        name: str,
        type: DependencyType,
        check: Callable[["Dependency"], dict[str, Any]],
    ) -> None:
        self._name = name
        self._type = type
        self._check = check
        self.depth: int = 0
        self.uri: Optional[str] = None
        self.custom_check: Optional[Callable[[], dict[str, Any]]] = None

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> DependencyType:
        return self._type

    @property
    def check(self) -> Callable[["Dependency"], dict[str, Any]]:
        return self._check
