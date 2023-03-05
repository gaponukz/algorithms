from __future__ import annotations

import unittest
import dataclasses
import typing

KT = typing.TypeVar("KT", bound=typing.Hashable) # key type
VT = typing.TypeVar("VT") # value type
DVT = typing.TypeVar("DVT") # default value type

@dataclasses.dataclass
class HashTableItem(typing.Generic[KT, VT]):
    key: KT
    value: VT
    next: HashTableItem[KT, VT] | None = None


class HashTable(typing.Generic[KT, VT]):
    __slots__ = 'size', 'storage'

    def __init__(self, **kwargs: VT):
        self.size: typing.Final[int] = 101111
        self.storage: list[HashTableItem[KT, VT] | None] = [None] * self.size

        for key in kwargs:
            self[key] = kwargs[key]

    def get(self, key: KT, default: DVT = None) -> VT | DVT:
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self, key: KT, default: DVT = None) -> VT | DVT:
        try:
            item = self[key]
            del self[key]
            return item
        except KeyError:
            return default

    def __getitem__(self, key: KT) -> VT:
        key_hash = hash(key) % self.size

        if (item := self.storage[key_hash]):
            for item in self.__walk_hashtable_items(item):
                if not item:
                    break

                if item.key == key:
                    return item.value

        raise KeyError(key)

    def __setitem__(self, key: KT, value: VT) -> None:
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

    def __contains__(self, key: KT) -> bool:
        try:
            self[key]
            return True
        except KeyError:
            return False

    def __delitem__(self, key: KT) -> None:
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


class TestHashTableMethods(unittest.TestCase):
    def test_all_aviable_methods(self):
        # create an instance of the HashTable class
        table = HashTable(init_key = 'init_value')

        # add some key-value pairs to the table
        table['key1'] = 'value1'
        table['key2'] = 'value2'
        table[3] = 'value3'
        table[101] = 'value4'
        
        # check if the initial key-value pair was added correctly
        self.assertEqual(table['init_key'], 'init_value')

        # check if other key-value pairs were added correctly
        self.assertEqual(table[3], 'value3')
        self.assertEqual(table['key1'], 'value1')
        self.assertEqual(table[101], 'value4')

        # check if a key is present in the table
        self.assertTrue('key2' in table)

        # check if KeyError is raised for a non-existent key
        with self.assertRaises(KeyError):
            table['key4']
        
        # delete a key-value pair from the table
        del table['key2']

        # check if the key was removed from the table
        self.assertTrue('key2' not in table)

        # check if KeyError is raised for a deleted key
        with self.assertRaises(KeyError):
            table['key2']
        
        # check if get() method returns None for a non-existent key
        self.assertEqual(table.get('key2'), None)

        # check if pop() method returns the correct value and removes the key-value pair
        self.assertEqual(table.pop(101), 'value4')

        # check if pop() method returns None for a non-existent key
        self.assertEqual(table.pop(101), None)


if __name__ == '__main__':
    # Why dict 17X faster but used 873815X more memory than my HashTable?
    unittest.main()
