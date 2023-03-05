# https://www.eolymp.com/uk/submissions/13065498

import sys
from collections import defaultdict

sys.stdin.readline()
mp = defaultdict(int)

for cur in map(int, sys.stdin.readline().split()):
    mp[cur] += 1

sys.stdin.readline()

for cur in map(int, sys.stdin.readline().split()):
    print(mp[cur])

