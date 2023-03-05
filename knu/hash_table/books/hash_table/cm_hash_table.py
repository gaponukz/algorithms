from __future__ import annotations
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
        next: A reference to the next item in chain.
    """
    key: typing.Hashable
    value: typing.Any
    next: typing.Optional[HashTableItem] = None


class HashTable:
    """ Chain method hash table implementation. """
    __slots__ = 'size', 'storage'

    def __init__(self, **kwargs: typing.Any):
        self.size: typing.Final = 101111
        self.storage: list[typing.Optional[HashTableItem]] = [None] * self.size

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

        if (item := self.storage[key_hash]):
            for item in self.__walk_hashtable_items(item):
                if not item:
                    break

                if item.key == key:
                    return item.value

        raise KeyError(key)

    def __setitem__(self, key: typing.Hashable, value: typing.Any) -> None:
        key_hash = hash(key) % self.size

        if not self.storage[key_hash]:
            self.storage[key_hash] = HashTableItem(key, value)
        else:
            item = self.storage[key_hash]

            for item in self.__walk_hashtable_items(item):
                if not item.next:
                    item.next = HashTableItem(key, value)
                    break

                if item.key == key:
                    item.value = value
                    break

    def __contains__(self, key: typing.Hashable) -> bool:
        try:
            self[key]
            return True
        except KeyError:
            return False

    def __delitem__(self, key: typing.Hashable) -> None:
        key_hash = hash(key) % self.size

        if (item := self.storage[key_hash]):
            for item in self.__walk_hashtable_items(item):
                if not item:
                    break

                if item.key == key:
                    self.storage[key_hash] = None
                    return

                if not item.next:
                    break

    def __walk_hashtable_items(self, root: HashTableItem) -> typing.Iterator[HashTableItem]:
        while root:
            yield root
            root = root.next
