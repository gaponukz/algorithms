# https://www.eolymp.com/uk/submissions/13250300

import dataclasses
import typing

T = typing.TypeVar("T", bound=int)

@dataclasses.dataclass
class HashTableItem:
    key: typing.Hashable
    value: typing.Any

class HashTable:
    __slots__ = 'size', 'storage'

    def __init__(self, **kwargs: typing.Any):
        self.size: typing.Final = 10001
        self.storage: list[list[HashTableItem]] = [[] for _ in range(self.size)]

        for key in kwargs:
            self[key] = kwargs[key]

    def get(self, key: typing.Hashable, default: typing.Any = None) -> typing.Any:
        try:
            return self[key]
        except KeyError:
            return default

    def __getitem__(self, key: typing.Hashable) -> typing.Any:
        key_hash = hash(key) % self.size

        for item in self.storage[key_hash]:
            if item.key == key:
                return item.value

        raise KeyError(key)

    def __setitem__(self, key: typing.Hashable, value: typing.Any) -> None:
        key_hash = hash(key) % self.size

        if not self.storage[key_hash]:
            self.storage[key_hash].append(HashTableItem(key, value))
        else:
            for item in self.storage[key_hash]:
                if item.key == key:
                    item.value = value
                    return
        
            self.storage[key_hash].append(HashTableItem(key, value))

    def __contains__(self, key: typing.Hashable) -> bool:
        try:
            self[key]
            return True
        except KeyError:
            return False

    def __delitem__(self, key: typing.Hashable) -> None:
        key_hash = hash(key) % self.size

        for item in self.storage[key_hash]:
            if item.key == key:
                self.storage[key_hash].remove(item)
                return
        
        raise KeyError(key)

def binary_search(data: list[T], x: T) -> T:
    low, high = 0, len(data) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] > x:
            result = data[mid]
            high = mid - 1

        else:
            low = mid + 1

    return result

def get_letters_info(string: str) -> HashTable:
    result = HashTable()

    for index, char in enumerate(string):
        if not result.get(char):
            result[char] = []
        
        result[char].append(index)

    return result

def main():
    n = int(input())
    obscene_words = [input() for _ in range(n)]
    text = input()

    text_letters_info = get_letters_info(text)
    result = None

    for word in obscene_words:
        indexes: list[int] = []

        for char in word:
            last = indexes[-1] if indexes else -1
            item = binary_search(text_letters_info.get(char, []), last)

            if item != -1:
                indexes.append(item)
            
            else:
                break
        
        else:
            num = indexes[-1] + 1
            result = result if result and result < num else num

    if result:
        print(f"YES {result}")

    else:
        print("NO")

if __name__ == "__main__":
    main()
