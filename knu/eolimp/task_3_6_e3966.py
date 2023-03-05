# https://www.eolymp.com/uk/submissions/13065447

import sys

sys.stdin.readline()
st = set(sys.stdin.readline().split()) # get element O(1)
sys.stdin.readline()
inp_set = sys.stdin.readline().split() # get element O(n)

for item in inp_set:
    print("YES" if item in st else "NO")
