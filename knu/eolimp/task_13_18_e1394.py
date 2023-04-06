# https://www.eolymp.com/uk/submissions/13443763

from __future__ import annotations

import typing
import dataclasses

class EmptyStackError(Exception):
    pass

class ConditionalError(Exception):
    pass

T = typing.TypeVar('T')

@dataclasses.dataclass
class Operation(typing.Generic[T]):
    action: typing.Callable[[T, T], T]
    property: int

@dataclasses.dataclass
class Node(typing.Generic[T]):
    item: T
    next: Node[T] | None = None

class Stack(typing.Generic[T]):
    def __init__(self):
        self.top_node: Node[T] | None = None
    
    def empty(self) -> bool:
        return self.top_node is None
    
    def push(self, item: T):
        new_node = Node(item)

        if not self.empty():
            new_node.next = self.top_node
        
        self.top_node = new_node
    
    def pop(self) -> T:
        if self.empty():
            raise EmptyStackError
        
        current_top = self.top_node
        item = current_top.item
        self.top_node = self.top_node.next

        del current_top
        return item
    
    def top(self) -> T:
        if self.empty():
            EmptyStackError
        
        return self.top_node.item

BRACKETS = typing.Literal['(', ')']
ALLOWED_OPERATORS = typing.Literal['+', '-', '*', '/']

class Calculator(typing.Generic[T]):
    def __init__(
            self,
            operations: dict[ALLOWED_OPERATORS, Operation[T]],
            tokenizer: typing.Callable[[str], list[ALLOWED_OPERATORS | T | BRACKETS]]
        ):
        
        self.operations = operations
        self.tokenizer = tokenizer
    
    def _convert_to_polish(self, _expression: str) -> list[ALLOWED_OPERATORS | T | BRACKETS]:
        expression: list[ALLOWED_OPERATORS | T | BRACKETS] = self.tokenizer(_expression)
        stack: Stack[ALLOWED_OPERATORS | T | BRACKETS] = Stack()
        postfix_list: list[ALLOWED_OPERATORS | T | BRACKETS] = []

        for token in expression:
            if token in self.operations:
                while not stack.empty():
                    prev: ALLOWED_OPERATORS = stack.top()

                    if prev in self.operations and \
                        self.operations[prev].property >= self.operations[token].property:
                        
                        stack.pop()
                        postfix_list.append(prev)
                    
                    else:
                        break
                
                stack.push(token)
            
            elif token == '(':
                stack.push(token)
            
            elif token == ')':
                it = stack.pop()

                while it != '(':
                    postfix_list.append(it)
                    it = stack.pop()
            
            else:
                postfix_list.append(token)
        
        while not stack.empty():
            postfix_list.append(stack.pop())
        
        return postfix_list

    def culculate(self, expression: str) -> T:
        expression = self._convert_to_polish(expression)
        stack: Stack[ALLOWED_OPERATORS | T | BRACKETS] = Stack()

        for token in expression:
            if token in self.operations:
                right_operand: T = stack.pop()
                left_operand: T = stack.pop()

                stack.push(self.operations[token].action(left_operand, right_operand))
            
            else:
                stack.push(token)
        
        return stack.pop()

OPERATORS: dict[ALLOWED_OPERATORS, Operation[int]] = {
    "+": Operation(property = 1, action = lambda a, b: check(a + b)),
    "-": Operation(property = 1, action = lambda a, b: check(a - b)),
    "*": Operation(property = 2, action = lambda a, b: check(a * b)),
    "/": Operation(property = 2, action = lambda a, b: check(a // b))
}

def check(result: int) -> int:
    if result < 0 or len(str(result)) > 90:
        raise ConditionalError("результат деякої операції від'ємний або перевищує 90 цифр")
    
    return result

def tokenize_expression(expression: str) -> list[ALLOWED_OPERATORS | int | BRACKETS]:
    result = []
    i = 0

    while i < len(expression):
        if expression[i].isdigit():
            j = i + 1

            while j < len(expression) and expression[j].isdigit():
                j += 1
            
            if len(expression[i:j]) > 90:
                raise ConditionalError("вхідне число перевищує 90 цифр")
            
            result.append(int(expression[i:j]))
            i = j

        elif expression[i] in '*(+/-)':
            result.append(expression[i])
            i += 1
        
        else:
            i += 1
        
    return result

if __name__ == '__main__':
    with open("output.txt", "w", encoding="utf-8") as out_stream:
        with open("input.txt", 'r', encoding='utf-8') as input_stream:
            calculator: Calculator[int] = Calculator(OPERATORS, tokenize_expression)

            for expression in input_stream:
                try:
                    result = check(calculator.culculate(expression))
                    out_stream.write(f"{result}\n")

                except (ZeroDivisionError, ConditionalError):
                    out_stream.write("Error\n")
