# https://www.eolymp.com/uk/submissions/13226697

from collections import defaultdict

s = input()
n = int(input())
mp = defaultdict(int)
for ch in s:
    mp[ch] += 1

ans = 0
for i in range(n):
    cur = input()
    success = True
    mcur = defaultdict(int)
    for ch in cur:
        mcur[ch] += 1
        if mcur[ch] > mp[ch]:
            success = False
            break

    if success:
        ans += 1

print(ans)
