# https://www.eolymp.com/uk/submissions/13610379

import abc
import typing

class SegmentTreeTemplate:
    def __init__(self, array: list[int]):
        self._array = array
        self._tree = [0] * (4 * len(array))
        self._build(0, 0, len(array) - 1)
        self._length = len(array)

    @abc.abstractmethod
    def strategy(self, a: int, b: int) -> int: ...

    @property
    @abc.abstractmethod
    def default(self) -> int: ...

    def _build(self, node, left, right):
        if left == right:
            self._tree[node] = self._array[left]
        
        else:
            mid = (left + right) // 2
            self._build(2 * node + 1, left, mid)
            self._build(2 * node + 2, mid + 1, right)
            self._tree[node] = self.strategy(self._tree[2 * node + 1], self._tree[2 * node + 2])

    def _query(self, node, left, right, q_left, q_right):
        if q_left <= left and q_right >= right:
            return self._tree[node]
        
        elif q_left > right or q_right < left:
            return self.default
        
        else:
            mid = (left + right) // 2
            return self.strategy(self._query(2 * node + 1, left, mid, q_left, q_right),
                            self._query(2 * node + 2, mid + 1, right, q_left, q_right))

    def _update(self, node, left, right, idx, val):
        if left == right:
            self._tree[node] = val

        else:
            mid = (left + right) // 2
            
            if idx <= mid:
                self._update(2 * node + 1, left, mid, idx, val)
            
            else:
                self._update(2 * node + 2, mid + 1, right, idx, val)
            
            self._tree[node] = self.strategy(self._tree[2 * node + 1], self._tree[2 * node + 2])

    def __setitem__(self, key: int, value: int):
        self._update(0, 0, len(self) - 1, key, value)
    
    def __getitem__(self, key: slice) -> int:
        start, stop, _ = key.indices(len(self))
        return self._query(0, 0, len(self) - 1, start, stop,)
    
    def __len__(self):
        return self._length

class GcdSegmentTree(SegmentTreeTemplate):
    default: typing.Final[int] = 0

    def strategy(self, a: int, b: int):
        if a == 0:
            return b
        
        return self.strategy(b % a, a)

class LcmSegmentTree(SegmentTreeTemplate):
    default: typing.Final[int] = 1

    def _gcd(self, a: int, b: int):
        if a == 0:
            return b
        return self._gcd(b % a, a)

    def strategy(self, a: int, b: int):
        return (a * b) // self._gcd(a, b)

if __name__ == '__main__':
    with open("output.txt", "w", encoding="utf-8") as out_stream:
        with open("input.txt", 'r', encoding='utf-8') as input_stream:
            n = int(input_stream.readline().strip())
            array = list(map(int, input_stream.readline().split()))
            m = int(input_stream.readline())
            
            fast_gcd = GcdSegmentTree(array)
            fast_lcm = LcmSegmentTree(array)

            for _ in range(m):
                q: typing.Literal[1, 2]
                l: int
                r: int

                q, l, r = list(map(int, input_stream.readline().split()))

                if q == 1:
                    l -= 1
                    r -= 1
                    vityas_number = fast_gcd[l:r]
                    guards_number = fast_lcm[l:r]

                    if vityas_number < guards_number:
                        out_stream.write(f"wins\n")  

                    elif guards_number < vityas_number:
                        out_stream.write(f"loser\n")  

                    else:
                        out_stream.write(f"draw\n")  
                
                else:
                    l -= 1
                    fast_gcd[l] = r
                    fast_lcm[l] = r
