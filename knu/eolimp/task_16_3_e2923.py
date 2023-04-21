# https://www.eolymp.com/uk/submissions/13560900

from __future__ import annotations

import typing
from collections import deque

K_T = typing.TypeVar("K_T")
V_T = typing.TypeVar("V_T")

class Tree(typing.Generic[K_T, V_T]):
    def __init__(self, key: K_T, value: V_T, parent: Tree = None):
        self._key = key
        self._value = value
        self._parent = parent
        self._children: list[Tree] = []

    def get_key(self) -> K_T:
        return self._key
    
    def get_value(self) -> V_T:
        return self._value
    
    def get_children(self) -> list[Tree]:
        return self._children
    
    def get_parent(self) -> Tree:
        return self._parent

    def bfs(self, key: K_T) -> Tree:
        queue: deque[Tree] = deque()
        queue.append(self)

        while queue:
            node = queue.popleft()

            if node.get_key() == key:
                return node
            
            for child in node.get_children():
                queue.append(child)

    def add(self, parent_key: K_T, key: K_T, value: V_T):
        par = self.bfs(parent_key)
        node = Tree(key, value, parent=par)
        
        par._children.append(node)

    def get(self, key1: K_T, key2: K_T) -> K_T:
        node = self.bfs(key1)
        came_from = None

        while node is not None:
            if node.get_key() == key2:
                return node.get_key()
            
            for child in node.get_children():
                if child is not came_from and child.bfs(key2) is not None:
                    return node.get_key()

            came_from = node
            node = node.get_parent()

# realization #
Color: typing.TypeAlias = int

def colours(tree: Tree[int, Color], colours_set: set[Color]):
    colours_set.add(tree.get_value())
    
    for child in tree.get_children():
        colours(child, colours_set)

if __name__ == "__main__":
    n = int(input())
    list_tree = []
    added = []

    for _ in range(n):
        list_tree.append([int(i) for i in input().split()])
        added.append(list_tree[-1][0])

    ind = added.index(0)
    t = list_tree[ind]
    list_tree[ind] = [-1, -1]
    added[ind] = -1
    tree: Tree[int, Color] = Tree(ind + 1, t[1])

    parents = [[ind + 1]]

    while list_tree:
        parents.append([])

        for j in parents[len(parents) - 2]:
            while True:
                try:
                    ind = added.index(j)
                    tree.add(j, ind + 1, list_tree[ind][1])
                    list_tree[ind] = [-1, -1]
                    added[ind] = -1

                    if ind + 1 not in parents[-1]:
                        parents[-1].append(ind + 1)
                    
                except ValueError:
                    break

        if all(map(lambda x: x == -1, added)):
            break

    result = []

    for i in range(1, len(list_tree) + 1):
        c = set()
        colours(tree.bfs(i), c)
        result.append(len(c))

    print(" ".join([str(i) for i in result]))
