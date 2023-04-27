from __future__ import annotations

import abc
import typing

K_T = typing.TypeVar('K_T')
V_T = typing.TypeVar('V_T')

class ITree(abc.ABC, typing.Generic[K_T, V_T]):
    @abc.abstractmethod
    def key(self) -> K_T: ...

    @abc.abstractmethod
    def value(self) -> V_T: ...

    @abc.abstractmethod
    def set_value(self, value: V_T | None = None): ...

    @abc.abstractmethod
    def get_child_by_key(self, key: K_T) -> ITree[K_T, V_T]: ...
    
    @abc.abstractmethod
    def add_child(self, child: ITree[K_T, V_T]): ...

    @abc.abstractmethod
    def remove_child_by_key(self, key: K_T): ...

    @abc.abstractclassmethod
    def remove_child(self, child: ITree[K_T, V_T]): ...

    @abc.abstractclassmethod
    def children(self) -> list[ITree[K_T, V_T]]: ...