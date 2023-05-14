# https://www.eolymp.com/uk/submissions/13717770
def kruskal(sr: list[tuple[int, tuple[int, int]]], n: int, m: int) -> list[tuple[int, int]]:
    res = []
    cost = 0
    tree_id = list(range(n))
    
    sr.sort()

    for i in range(m):
        _, (a, b) = sr[i]
        if tree_id[a] != tree_id[b]:
            cost += 1
            res.append((a, b))
            old_id, new_id = tree_id[b], tree_id[a]
            
            for j in range(n):
                if tree_id[j] == old_id:
                    tree_id[j] = new_id
            
        if cost == n - 1:
            break

    return res

if __name__ == '__main__':
    n, m = map(int, input().split())

    sr = [(1, (a - 1, b - 1)) for a, b in [map(int, input().split()) for _ in range(m)]]

    res = kruskal(sr, n, m)
    for a, b in res:
        print(a + 1, b + 1)

