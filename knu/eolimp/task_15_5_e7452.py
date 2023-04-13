# https://www.eolymp.com/uk/submissions/13500886

from __future__ import annotations
import typing
import dataclasses

T = typing.TypeVar('T')

@dataclasses.dataclass
class Node(typing.Generic[T]):
    item: T
    next: Node[T] | None = None
    prev: Node[T] | None = None

class LinkedList(typing.Generic[T]):
    def __init__(self) -> None:
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None

    def append(self, item: T) -> None:
        new_node = Node(item)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def print(self) -> None:
        current = self.head
        
        while current:
            print(current.item, end=' ')
            current = current.next

        print()

    def print_reverse(self) -> None:
        current = self.tail
        
        while current:
            print(current.item, end=' ')
            current = current.prev
        
        print()

if __name__ == '__main__':
    input()
    
    linked_list: LinkedList[int] = LinkedList()
    
    for n in input().split():
        linked_list.append(int(n))

    linked_list.print()
    linked_list.print_reverse()
