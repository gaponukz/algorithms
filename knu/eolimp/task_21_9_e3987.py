# https://www.eolymp.com/uk/submissions/13650437
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

flag = True

for i in range(1, n + 1):
    used = [False] * (n + 1)
    ans = 1
    used[i] = True
    
    for node in graph[i]:
        if not used[node]:
            used[node] = True
            ans += 1
    
    if ans != n:
        flag = False
        break

print("YES" if flag else "NO")
