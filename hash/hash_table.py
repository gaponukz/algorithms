from __future__ import annotations

import unittest
import dataclasses
import typing

@dataclasses.dataclass
class HashTableItem:
    key: typing.Hashable
    value: typing.Any
    is_valid: bool = True
    next: HashTableItem = None

class HashTable:
    def __init__(self, size=9973):
        self.size: int = size
        self.storage: list[HashTableItem] = [None] * size
    
    def get(self, key: typing.Hashable, defaul: typing.Any=None):
        try:
            return self[key]
        
        except KeyError:
            return defaul

    def __find_item(self, key: typing.Hashable) -> HashTableItem:
        key_hash = hash(key) % self.size

        if (item := self.storage[key_hash]):
            while ...:
                if not item:
                    break

                if item.key == key:
                    return item

                item = item.next

        raise KeyError(key)

    def __setitem__(self, key: typing.Hashable, value: typing.Any) -> None:
        key_hash = hash(key) % self.size

        if not self.storage[key_hash]:
            self.storage[key_hash] = HashTableItem(key, value)
        
        else:
            item = self.storage[key_hash]

            while ...:
                if not item.next:
                    item.next = HashTableItem(key, value)
                    break
                
                if item.is_valid and item.key == key:
                    item.value = value
                    break
                
                item = item.next

    def __getitem__(self, key: typing.Hashable) -> typing.Any:
        item = self.__find_item(key)

        if not item.is_valid:
            raise KeyError(key)
        
        return item.value
    
    def __contains__(self, key: typing.Hashable) -> bool:
        try:
            item = self.__find_item(key)
            return item.is_valid
        
        except KeyError:
            return False
    
    def __delitem__(self, key: typing.Hashable) -> None:
        item = self.__find_item(key)
        item.is_valid = False

class TestHashTableMethods(unittest.TestCase):
    def test_all_aviable_methods(self):
        table = HashTable()
        table['key1'] = 'value1'
        table['key2'] = 'value2'
        table[3] = 'value3'
        table[101] = 'value4'
        
        self.assertEqual(table[3], 'value3')
        self.assertEqual(table['key1'], 'value1')
        self.assertEqual(table[101], 'value4')

        self.assertTrue('key2' in table)

        with self.assertRaises(KeyError):
            table['key4']
        
        del table['key2']

        self.assertTrue('key2' not in table)

        with self.assertRaises(KeyError):
            table['key2']
        
        self.assertEqual(table.get('key2'), None)

if __name__ == '__main__':
    unittest.main()
