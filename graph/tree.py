from __future__ import annotations

import typing
import collections

from interfaces import ITree

K_T = typing.TypeVar('K_T')
V_T = typing.TypeVar('V_T')

class Node(typing.Generic[K_T, V_T]):
    def __init__(self, key: K_T, value: V_T | None = None):
        self._key = key
        self._value = value
    
    def key(self) -> K_T:
        return self._key
    
    def value(self) -> V_T:
        return self._value
    
    def set_value(self, value: V_T | None = None):
        self._value = value
    
    def __str__(self):
        return f"{self.__class__.__name__}(key={self._key}, value={self._value})"

class Tree(Node[K_T, V_T], ITree[K_T, V_T]):
    def __init__(self, key: K_T, value: V_T | None = None):
        super().__init__(key, value)
        self._children: list[ITree[K_T, V_T]] = []

    def get_child_by_key(self, key: K_T) -> ITree[K_T, V_T]:
        for child in self._children:
            if child.key() == key:
                return child
        
        raise KeyError(key)

    def add_child(self, child: ITree[K_T, V_T]):
        self._children.append(child)
    
    def remove_child_by_key(self, key: K_T):
        self.remove_child(self.get_child_by_key(key))

    def remove_child(self, child: ITree[K_T, V_T]):
        self._children.remove(child)
    
    def children(self) -> list[ITree[K_T, V_T]]:
        return self._children

class UnorderedTree(Node[K_T, V_T], ITree[K_T, V_T]):
    def __init__(self, key: K_T, value: V_T | None = None):
        super().__init__(key, value)
        self._children: dict[K_T, ITree[K_T, V_T]] = {}

    def get_child_by_key(self, key: K_T) -> ITree[K_T, V_T]:
        if key in self._children:
            return self._children[key]
        
        raise KeyError(key)

    def add_child(self, child: ITree[K_T, V_T]):
        self._children[child.key()] = child
    
    def remove_child_by_key(self, key: K_T):
        self.remove_child(self.get_child_by_key(key))

    def remove_child(self, child: ITree[K_T, V_T]):
        del self._children[child.key()]
    
    def children(self) -> list[ITree[K_T, V_T]]:
        return list(self._children.values())

def print_dfs(root: ITree):
    print(root, end=' -> ')

    for child in root.children():
        print_dfs(child)

def print_bfs(root: ITree):
    queue = collections.deque[ITree]()
    queue.append(root)
    
    while queue:
        node = queue.pop()
        print(node, end=' -> ')

        for child in node.children():
            queue.append(child)

def search(root: ITree, element: ITree) -> bool:
    queue = collections.deque[ITree]()
    queue.append(root)

    while queue:
        node = queue.pop()

        if node.key() == element.key():
            return True
        
        for child in node.children():
            queue.append(child)
    
    return False

if __name__ == "__main__":
    node7 = Tree[int, None](7)
    node9 = Tree[int, None](9)
    node10 = Tree[int, None](10)
    node11 = Tree[int, None](11)
    node12 = Tree[int, None](12)
    node13 = Tree[int, None](13)
    node14 = Tree[int, None](14)
    node15 = Tree[int, None](15)
    node8 = Tree[int, None](8)
    node8.add_child(node14)
    node8.add_child(node15)
    node4 = Tree[int, None](4)
    node4.add_child(node8)
    node4.add_child(node9)
    node5 = Tree[int, None](5)
    node5.add_child(node10)
    node5.add_child(node11)
    node2 = Tree[int, None](2)
    node2.add_child(node4)
    node2.add_child(node5)
    node6 = Tree[int, None](6)
    node6.add_child(node12)
    node6.add_child(node13)
    node3 = Tree[int, None](3)
    node3.add_child(node6)
    node3.add_child(node7)
    root = Tree[int, None](1)
    root.add_child(node2)
    root.add_child(node3)

    print(search(root, Tree[int, None](5)))
