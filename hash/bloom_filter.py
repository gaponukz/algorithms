import math
import mmh3


class BloomFilter:
    def __init__(self, capacity: int, false_positive_rate: float) -> None:
        self.capacity: int = capacity
        self.false_positive_rate: float = false_positive_rate
        self.bit_array: list[bool] = [False] * self.__get_size(capacity, false_positive_rate)
        self.num_hashes: int = self.__get_hash_count(len(self.bit_array), capacity)

    def __get_size(self, capacity: int, false_positive_rate: float) -> int:
        m: float = - (capacity * math.log(false_positive_rate)) / (math.log(2) ** 2)
        return int(m)

    def __get_hash_count(self, m: int, n: int) -> int:
        k: float = (m / n) * math.log(2)
        return int(k)

    def _hash(self, item: str) -> list[int]:
        hashes: list[int] = []

        for i in range(self.num_hashes):
            # Use MurmurHash3 to generate a 32-bit hash value
            hash_value = mmh3.hash(item, i) & 0xffffffff
            hashes.append(hash_value)

        return hashes

    def add(self, item: str) -> None:
        for _hash in self._hash(item):
            index: int = _hash % len(self.bit_array)
            self.bit_array[index] = True

    def __contains__(self, item: str) -> bool:
        for _hash in self._hash(item):
            index = _hash % len(self.bit_array)

            if not self.bit_array[index]:
                return False
            
        return True
