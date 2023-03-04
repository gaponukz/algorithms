import math
import mmh3


class BloomFilter:
    __slots__ = 'capacity', 'false_positive_rate', 'bit_array', 'num_hashes'

    def __init__(self, capacity: int, false_positive_rate: float) -> None:
        self.capacity: int = capacity
        self.false_positive_rate: float = false_positive_rate
        self.bit_array: list[bool] = [False] * self.__get_size(capacity, false_positive_rate)
        self.num_hashes: int = self.__get_hash_count(len(self.bit_array), capacity)

    def hash_family(self, item: str) -> list[int]:
        hashes: list[int] = []

        for i in range(self.num_hashes):
            hash_value = mmh3.hash(item, i) & 0xffffffff
            hashes.append(hash_value)

        return hashes

    def add(self, item: str) -> None:
        for _hash in self.hash_family(item):
            index: int = _hash % len(self.bit_array)
            self.bit_array[index] = True
    
    def append(self, item: str) -> None:
        self.add(item)

    def __contains__(self, item: str) -> bool:
        for _hash in self.hash_family(item):
            index = _hash % len(self.bit_array)

            if not self.bit_array[index]:
                return False
            
        return True

    def __get_size(self, capacity: int, false_positive_rate: float) -> int:
        m: float = - (capacity * math.log(false_positive_rate)) / (math.log(2) ** 2)
        return int(m)

    def __get_hash_count(self, m: int, n: int) -> int:
        k: float = (m / n) * math.log(2)
        return int(k)


if __name__ == "__main__":
    # test is and compare wiht list
    import time
    import sys

    data = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tortor lorem, accumsan a congue ut, consectetur non ipsum. Proin hendrerit finibus dui ac consectetur. Phasellus consequat massa justo, sit amet eleifend orci bibendum non. Suspendisse nec finibus justo, consequat porttitor neque. Ut id libero odio. Nulla ac ante condimentum, hendrerit justo non, congue velit. Suspendisse potenti. Vestibulum suscipit congue tincidunt. Ut ultricies lorem dui, sit amet faucibus massa viverra quis. Morbi consequat vehicula nisi, a mattis massa. Morbi nec velit accumsan, feugiat mi eu, pulvinar massa. Praesent bibendum tempor dui et convallis. Maecenas posuere risus nec faucibus eleifend. Maecenas neque risus, sagittis a urna vel, laoreet malesuada nisl. Donec rhoncus, elit id lacinia euismod, metus tortor ultricies arcu, non malesuada ex odio eu odio. Vivamus feugiat tellus vitae tincidunt egestas. Aliquam sit amet dolor pulvinar, venenatis dui ut, tempus orci. Etiam facilisis auctor diam, et vehicula libero fringilla quis. Morbi venenatis interdum metus. Praesent vitae varius nisl. Donec mollis orci ut turpis euismod tristique. Cras ultricies, lorem aliquam iaculis congue, dolor felis eleifend neque, in vehicula metus lacus suscipit nunc. Proin rhoncus dui id cursus pharetra. Fusce massa nulla, rhoncus in rhoncus nec, mattis ac ipsum. Cras dapibus rutrum dolor, nec cursus mi porttitor id. Donec tincidunt leo dui, nec laoreet mi commodo non. Nunc ultricies vel eros quis luctus. Sed lacinia venenatis eros vulputate consectetur. Praesent vulputate purus vitae sem pharetra, sed varius massa aliquam. Donec a condimentum nunc. Aliquam erat volutpat. Praesent orci urna, tristique nec accumsan et, dictum vitae orci. Aliquam ornare dictum enim imperdiet sagittis. Sed at orci quis nisi ullamcorper ultricies sed eu nisl. Praesent tristique venenatis elit ac lobortis. Ut congue porta ligula eu malesuada. Phasellus iaculis erat sit amet justo venenatis dapibus. Praesent id justo sit amet lacus elementum volutpat vitae at libero. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus a congue mi. Vivamus lacus ipsum, convallis non sem in, luctus facilisis diam. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;"""

    bfilter = BloomFilter(400, 0.01)

    for word in data.split():
        bfilter.append(word)
    
    start = time.time()
    'metus' in bfilter
    'luctus' in bfilter
    'lol' in bfilter
    print(time.time() - start)

    start = time.time()
    'metus' in data
    'luctus' in data
    'lol' in data
    print(time.time() - start)

    print(sys.getsizeof(bfilter), sys.getsizeof(data))
