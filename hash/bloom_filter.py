import math
import mmh3


class BloomFilter:
    __slots__ = 'capacity', 'false_positive_rate', 'bit_array', 'num_hashes'

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
    
    def append(self, item: str) -> None:
        self.add(item)

    def __contains__(self, item: str) -> bool:
        for _hash in self._hash(item):
            index = _hash % len(self.bit_array)

            if not self.bit_array[index]:
                return False
            
        return True

if __name__ == "__main__":
    # test is and compare wiht list
    import time

    data = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tortor lorem, accumsan a congue ut, consectetur non ipsum. Proin hendrerit finibus dui ac consectetur. Phasellus consequat massa justo, sit amet eleifend orci bibendum non. Suspendisse nec finibus justo, consequat porttitor neque. Ut id libero odio. Nulla ac ante condimentum, hendrerit justo non, congue velit. Suspendisse potenti. Vestibulum suscipit congue tincidunt. Ut ultricies lorem dui, sit amet faucibus massa viverra quis. Morbi consequat vehicula nisi, a mattis massa. Morbi nec velit accumsan, feugiat mi eu, pulvinar massa. Praesent bibendum tempor dui et convallis. Maecenas posuere risus nec faucibus eleifend. Maecenas neque risus, sagittis a urna vel, laoreet malesuada nisl. Donec rhoncus, elit id lacinia euismod, metus tortor ultricies arcu, non malesuada ex odio eu odio. Vivamus feugiat tellus vitae tincidunt egestas. Aliquam sit amet dolor pulvinar, venenatis dui ut, tempus orci. Etiam facilisis auctor diam, et vehicula libero fringilla quis. Morbi venenatis interdum metus. Praesent vitae varius nisl. Donec mollis orci ut turpis euismod tristique."""

    bfilter = BloomFilter(200, 0.01)

    for word in data.split():
        bfilter.append(word)
    
    start = time.time()
    print('metus' in bfilter)
    print(time.time() - start)

    start = time.time()
    print('metus' in data)
    print(time.time() - start)
