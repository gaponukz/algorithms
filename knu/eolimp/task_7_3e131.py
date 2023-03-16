# https://www.eolymp.com/uk/submissions/13250383
import dataclasses
import typing

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


s = input()
n = int(input())
mp = HashTable()

for ch in s:
    if not mp.get(ch):
        mp[ch] = 0
    
    mp[ch] += 1

ans = 0
for i in range(n):
    cur = input()
    success = True
    mcur = HashTable()
    for ch in cur:
        if not mcur.get(ch):
            mcur[ch] = 0
        
        if not mp.get(ch):
            mp[ch] = 0
        
        mcur[ch] += 1
        if mcur[ch] > mp[ch]:
            success = False
            break

    if success:
        ans += 1

print(ans)
