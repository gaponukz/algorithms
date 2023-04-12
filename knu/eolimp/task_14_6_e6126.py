# https://www.eolymp.com/uk/submissions/13489351

from __future__ import annotations

import typing
import dataclasses

T = typing.TypeVar('T')

@dataclasses.dataclass
class Node(typing.Generic[T]):
    item: T
    next: Node[T] | None = None

class Queue(typing.Generic[T]):
    def __init__(self):
        self.front: Node[T] | None = None
        self.back: Node[T] | None = None
        self._lenght = 0
    
    def first(self) -> T:
        return self.front.item
    
    def empty(self) -> bool:
        return self._lenght == 0

    def clear(self):
        self._lenght = 0
        self.front = None
        self.back = None
    
    def enqueue(self, item: T):
        new_node = Node(item)

        if self.empty():
            self.front = new_node
        
        else:
            self.back.next = new_node

        self._lenght += 1
        self.back = new_node
    
    def dequeue(self) -> T:
        if self.empty():
            raise ValueError("Empty queue")

        current_front = self.front
        item = current_front.item
        self.front = self.front.next

        del current_front

        if self.front is None:
            self.back = None
        
        self._lenght -= 1

        return item

    def __len__(self):
        return self._lenght

if __name__ == "__main__":
    with open("output.txt", "w", encoding="utf-8") as out_stream:
        with open("input.txt", 'r', encoding='utf-8') as input_stream:
            deque: Queue[str] = Queue()
            
            for line in input_stream:
                if line.startswith("exit"):
                    out_stream.write(f"bye\n")
                    break
                
                try:
                    if line.startswith("push"):
                        deque.enqueue(line.split()[-1])
                        out_stream.write(f"ok\n")
                    
                    elif line.startswith("pop"):
                        out_stream.write(f"{deque.dequeue()}\n")
                    
                    elif line.startswith("front"):
                        out_stream.write(f"{deque.first()}\n")
                    
                    elif line.startswith("size"):
                        out_stream.write(f"{len(deque)}\n")

                    elif line.startswith("clear"):
                        deque.clear()
                        out_stream.write(f"ok\n")
                
                except:
                    out_stream.write(f"error\n")
