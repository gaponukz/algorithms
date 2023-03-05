import math

# 1.4 a
def a(n):
    if n == 0:
        return 1
    return a(n - 1) + pow(2, n)

def a1(n):
    return pow(2, n + 1) - 1

for i in range(1, 5):
    assert a(i) == a1(i)

# 1.4 c
def c(n):
    if n == 1:
        return 1
    return 2 * c(int(n / 2)) + 1

def c1(n):
    return pow(2, 1 + int(math.log2(n))) - 1

for i in range(1, 5):
    assert c(i) == c1(i)

# 1.4 d
def d(n, a):
    return pow(a, n + int(math.log(n, a))) - 1
