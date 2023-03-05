# https://www.eolymp.com/uk/submissions/13064929

import sys

for line in sys.stdin:
    n: int = int(line)
    v: list[int] = list(map(int, input().split()))
    a, b = map(int, input().split())

    ans = 0

    for i in range(n):
        if v[i] >= a and v[i] <= b:
            ans += 1
    
    print(ans)
