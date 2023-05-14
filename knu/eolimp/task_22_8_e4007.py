# https://www.eolymp.com/uk/submissions/13717803
from queue import Queue

def check(n, cur, b, parr, q):
    if n == b and n not in parr:
        parr[n] = cur
        q.put(n)
        return True
    
    elif n == b:
        return True
    
    elif n not in parr:
        parr[n] = cur
        q.put(n)
        return False
    
    elif n in parr:
        return False


def bfs(a, b):
    q = Queue()
    q.put(a)

    parr = {}
    parr[a] = -1

    while not q.empty():
        cur = q.get()

        if cur // 1000 != 9:
            n = (cur // 1000 + 1) * 1000 + cur % 1000
            if check(n, cur, b, parr, q):
                break

        if cur % 10 != 1:
            n = cur - 1
            if check(n, cur, b, parr, q):
                break

        n = cur // 10 + (cur % 10) * 1000
        if check(n, cur, b, parr, q):
            break

        n = (cur % 1000) * 10 + (cur // 1000)
        if check(n, cur, b, parr, q):
            break

    if b not in parr:
        print(-1)
        return

    st = []
    cur = b
    while cur != a:
        st.append(cur)
        cur = parr[cur]

    st.append(a)
    for i in range(len(st) - 1, -1, -1):
        print(st[i])


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    
    bfs(a, b)
