# https://www.eolymp.com/uk/submissions/13124997

import sys

n, k = map(int, sys.stdin.readline().split())
v = list()
for _ in range(n):
    v.append(int(sys.stdin.readline()))

v.sort(reverse=True)

def success(dist):
    ans = 0
    for i in range(n):
        if v[i] < dist:
            break
        else:
            ans += v[i] // dist
    return ans >= k

l, r = 0, 10000000
while r - l > 1:
    mid = (r + l) // 2
    if success(mid):
        l = mid
    else:
        r = mid

l = l + 1 if success(l + 1) else l
print(l)
