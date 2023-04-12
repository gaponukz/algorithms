# https://www.eolymp.com/uk/submissions/13490379
from collections import deque

Stack = deque[tuple[int, int]]

def min_queue_getMin(s1: Stack, s2: Stack) -> int:
    if not s1 and not s2:
        return 0
    
    elif not s1 or not s2:
        return s2[-1][1] if not s1 else s1[-1][1]
    
    else:
        return min(s1[-1][1], s2[-1][1])

def min_queue_pop(s1: Stack, s2: Stack) -> None:
    if not s2:
        while s1:
            element, _ = s1.pop()
            minima = element if not s2 else min(element, s2[-1][1])
            s2.append((element, minima))
    
    if s2:
        s2.pop()

def min_queue_add(s1: Stack, new_element: int) -> None:
    minima = new_element if not s1 else min(new_element, s1[-1][1])
    s1.append((new_element, minima))

if __name__ == '__main__':
    n, a, b, c, cur_x = map(int, input().split())
    mod = 1000 * 1000
    ans = 0
    s1, s2 = deque(), deque()

    for i in range(n):
        cur = ((a * cur_x * cur_x + b * cur_x + c) // 100) % mod
        cur_x = cur
        if cur_x % 5 < 2:
            min_queue_pop(s1, s2)
        
        else:
            min_queue_add(s1, cur_x)
        
        ans += min_queue_getMin(s1, s2)
    
    print(ans)

