# https://www.eolymp.com/uk/submissions/13441345

def get_char_digit(digit: int) -> str:
    return str(digit) if digit <= 9 else f"[{digit}]"

def contert(dec_number: int, base: int) -> str:
    stack = []

    while dec_number > 0:
        stack.append(dec_number % base)
        dec_number //= base
    
    conevrted = ''

    while stack:
        conevrted += get_char_digit(stack.pop())
    
    return conevrted

if __name__ == '__main__':
    dec_number = int(input())
    base = int(input())
    
    print(contert(dec_number, base))
