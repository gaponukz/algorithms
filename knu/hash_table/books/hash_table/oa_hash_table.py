from .hash_table_interface import IHashTable

import dataclasses
import typing

@dataclasses.dataclass
class HashTableItem(IHashTable):
    """
    Data class for a hash table item.

    Attributes:
        key: A hashable key used for lookup.
        value: The value associated with the key.
    """
    key: typing.Hashable
    value: typing.Any


class HashTable:
    """ Open addressing method hash table implementation. """
    __slots__ = 'size', 'storage'

    def __init__(self, **kwargs: typing.Any):
        self.size: typing.Final = 3
        self.storage: list[list[HashTableItem]] = [[] for _ in range(self.size)]

        for key in kwargs:
            self[key] = kwargs[key]

    def get(self, key: typing.Hashable, default: typing.Any = None) -> typing.Any:
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self, key: typing.Hashable, default: typing.Any = None) -> typing.Any:
        try:
            item = self[key]
            del self[key]
            return item
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
