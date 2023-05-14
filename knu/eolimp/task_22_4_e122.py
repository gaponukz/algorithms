# https://www.eolymp.com/uk/submissions/13717725
n, m, start, finish, d = map(int, input().split())
start, finish = start - 1, finish - 1

ss = [[] for _ in range(n)]
color = [0] * n
ans = 0

def dfs(node: int, length: int) -> None:
    global ans

    if node == finish and length <= d:
        ans += 1
        return
    if length > d:
        return

    color[node] = 1
    for child in ss[node]:
        if color[child] == 0 or color[child] == 2:
            dfs(child, length + 1)

    color[node] = 2

for i in range(m):
    a, b = map(int, input().split())
    ss[a - 1].append(b - 1)

dfs(start, 0)
print(ans)
