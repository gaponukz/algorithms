# https://www.eolymp.com/uk/submissions/13650324
n = int(input())
graph = [[] for _ in range(n)]

for i in range(n):
    row = input().split()
    for j in range(n):
        a = int(row[j])
        if j >= i and a > 0:
            graph[i].append(j)
            graph[j].append(i)

ans = 0

for i in range(n):
    if len(graph[i]) == 1:
        ans += 1

print(ans)
