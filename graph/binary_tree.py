from __future__ import annotations

import typing

T = typing.TypeVar('T')

class BinaryTree(typing.Generic[T]):
    def __init__(self, key: T):
        self._key = key
        self._left_child: BinaryTree | None = None
        self._right_child: BinaryTree | None = None
        self._parent: BinaryTree | None = None
    
    def has_left_child(self) -> bool:
        return self._left_child is not None
        
    def has_right_child(self) -> bool:
        return self._right_child is not None
    
    def has_children(self) -> bool:
        return self.has_left_child() and self.has_right_child()
    
    ...