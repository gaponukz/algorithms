# https://www.eolymp.com/uk/submissions/13650414

n, m = map(int, input().split())
graph = dict[tuple[int, int], int]()

success = False

for i in range(m):
    a, b = map(int, input().split())
    
    if (a, b) in graph:
        success = True
    
    graph[(a, b)] = graph.get((a, b), 0) + 1

print("YES" if success else "NO")