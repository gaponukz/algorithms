# https://www.eolymp.com/uk/submissions/13501348

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
        self._length = 0

    def append(self, item: T) -> None:
        new_node = Node(item)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self._length += 1

    def rotate_right(self, k: int) -> None:
        if not self.head or k == 0:
            return
        
        k %= self._length

        if k == 0:
            return
        
        current = self.head
        for _ in range(self._length - k - 1):
            current = current.next

        new_tail = current
        new_head = current.next

        new_tail.next = None
        new_head.prev = None
        self.tail.next = self.head
        self.head.prev = self.tail
        self.head = new_head
        self.tail = new_tail
    
    def __str__(self):
        result = ""
        current = self.head
        
        while current:
            result += f"{current.item} "
            current = current.next

        return result.removesuffix(" ")

if __name__ == '__main__':
    with open("output.txt", "w", encoding="utf-8") as out_stream:
        with open("input.txt", 'r', encoding='utf-8') as input_stream:
            n = int(input_stream.readline())
            linked_list: LinkedList[int] = LinkedList()
            
            for item in input_stream.readline().split():
                linked_list.append(int(item))
            
            for line in input_stream:
                if not line:
                    continue

                linked_list.rotate_right(int(line))
                out_stream.write(f"{linked_list}\n")
