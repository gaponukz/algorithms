# https://www.eolymp.com/uk/submissions/13064790

a: int = int(input())
t = a
pow = 1

while t:
    t //= 2
    pow *= 2

t = a

maximum = a

while t != a or maximum == a:
    a <<= 1
    a = a % pow + (1 if a >= pow else 0)
    if maximum < a:
        maximum = a

print(maximum)