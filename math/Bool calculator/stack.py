from typing import Any, Optional

class Node:
    def __init__(self, item: Any):
        self.item = item
        self.next: Optional['Node'] = None

class Stack:
    def __init__(self):
        self.top_node: Optional[Node] = None

    def empty(self) -> bool:
        return self.top_node is None
    
    def push(self, item: Any):
        new_node = Node(item)

        if not self.empty():
            new_node.next = self.top_node
    
        self.top_node = new_node
    
    def pop(self):
        if self.empty():
            raise Exception("Stack: 'pop' applied to empty container")
        
        current_top = self.top_node
        item = current_top.item
        self.top_node = self.top_node.next

        del current_top
        return item
    
    def top(self):
        if self.empty():
            raise Exception("Stack: 'top' applied to empty container")
        
        return self.top_node.item
