# https://www.eolymp.com/uk/submissions/13650361
n, m = map(int, input().split())

ss_vx = [[] for _ in range(n)]
ss_vy = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ss_vy[a].append(b)
    ss_vx[b].append(a)

for i in range(n):
    print(len(ss_vx[i]), len(ss_vy[i]))
