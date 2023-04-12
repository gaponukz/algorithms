import nltk
from stack import Stack

OPERATORS = {
    "or": {
        "priority": 1,
        "function": lambda a, b: a or b
    },
    "and": {
        "priority": 2,
        "function": lambda a, b: a and b
    },
    "not": {
        "priority": 3,
        "function": lambda _, b: not b
    },
    "impl": {
        "priority": 0,
        "function": lambda a, b: not a or b
    },
    "xor": {
        "priority": 0,
        "function": lambda a, b: a ^ b
    },
    "eq": {
        "priority": 0,
        "function": lambda a, b: a == b
    }
}

class Expression(object):
    def __init__(self, str_expression: str):
        self.str_expression = str_expression
        self.converted_expression = self.convert()
    
    def convert(self):
        infix_list: list[str] = nltk.tokenize.word_tokenize(self.str_expression)
        postfix_list = []
        stack = Stack()

        for token in infix_list:
            if token in OPERATORS:
                while not stack.empty():
                    prev = stack.top()

                    if prev in OPERATORS and OPERATORS[prev]['priority'] >= OPERATORS[token]['priority']:
                        stack.pop()
                        postfix_list.append(prev) 
                    
                    else:
                        break
                
                stack.push(token)
            
            elif token == "(":
                stack.push(token)
            
            elif token == ")":
                it = stack.pop()

                while it != "(":
                    postfix_list.append(it)
                    it = stack.pop()
            
            else:
                postfix_list.append(token)

        while not stack.empty():
            postfix_list.append(stack.pop())

        return postfix_list
    
    def operation(self, left: bool, right: bool, operator: str) -> bool:
        assert operator in OPERATORS

        left, right = bool(int(left)), bool(int(right))
        
        return OPERATORS[operator]['function'](left, right)

    def apply(self):
        stack = Stack()

        for token in self.converted_expression:
            if token in OPERATORS:
                if token == "not":
                    right_operand = stack.pop()
                    
                    res = self.operation(0, right_operand, token)
                
                else:
                    right_operand = stack.pop()
                    left__operand = stack.pop()
                    
                    res = self.operation(left__operand, right_operand, token)

                stack.push(res)
            
            else:
                stack.push(token)
            
        return stack.pop()
