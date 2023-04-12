# https://www.eolymp.com/uk/submissions/13489527
from __future__ import annotations

import typing
import dataclasses

T = typing.TypeVar('T')

@dataclasses.dataclass
class Node(typing.Generic[T]):
    item: T
    next: Node[T] | None = None
    prev: Node[T] | None = None

class Queue(typing.Generic[T]):
    def __init__(self):
        self.front: Node[T] | None = None
        self.back: Node[T] | None = None
        self._lenght: int = 0
    
    def first(self) -> T:
        return self.front.item

    def last(self) -> T:
        return self.back.item
    
    def empty(self) -> bool:
        return self._lenght == 0

    def clear(self):
        self._lenght = 0
        self.front = None
        self.back = None
    
    def push(self, item: T):
        '''
        Add element to back
        '''
        new_node = Node(item)
        new_node.prev = self.back

        if not self.empty():
            self.back.next = new_node
        
        else:
            self.front = new_node

        self._lenght += 1
        self.back = new_node
    
    def pushleft(self, item: T):
        '''
        Add element to start
        '''
        new_node = Node(item)
        new_node.next = self.front

        if not self.empty():
            self.front.prev = new_node
        
        else:
            self.back = new_node
        
        self._lenght += 1
        self.front = new_node

    def pop(self) -> T:
        '''
        Remove element from end
        '''
        if self.empty():
            raise ValueError("Empty queue")

        node = self.back
        item = node.item
        self.back = node.prev

        if self.back is None:
            self.front = None
        
        self._lenght -= 1

        del node
        return item
    
    def popleft(self) -> T:
        '''
        Remove element from start
        '''
        if self.empty():
            raise ValueError("Empty queue")
        
        node = self.front
        item = node.item
        self.front = node.next

        if self.front is None:
            self.back = None

        else:
            self.front.prev = None
        
        self._lenght -= 1

        del node
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
                    if line.startswith("push_front"):
                        deque.pushleft(line.split()[-1])
                        out_stream.write(f"ok\n")

                    if line.startswith("push_back"):
                        deque.push(line.split()[-1])
                        out_stream.write(f"ok\n")
                    
                    elif line.startswith("pop_front"):
                        out_stream.write(f"{deque.popleft()}\n")

                    elif line.startswith("pop_back"):
                        out_stream.write(f"{deque.pop()}\n")
                    
                    elif line.startswith("front"):
                        out_stream.write(f"{deque.first()}\n")

                    elif line.startswith("back"):
                        out_stream.write(f"{deque.last()}\n")
                    
                    elif line.startswith("size"):
                        out_stream.write(f"{len(deque)}\n")

                    elif line.startswith("clear"):
                        deque.clear()
                        out_stream.write(f"ok\n")
                
                except:
                    out_stream.write(f"error\n")
