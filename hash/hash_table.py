from __future__ import annotations

import unittest
import dataclasses
import typing

@dataclasses.dataclass
class HashTableItem:
    key: typing.Hashable
    value: typing.Any
    next: HashTableItem = None

def walk_hashtable_items(root: HashTableItem) -> HashTableItem:
    while root:
        yield root
        root = root.next

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
            for item in walk_hashtable_items(item):
                if not item:
                    break

                if item.key == key:
                    return item

        raise KeyError(key)

    def __setitem__(self, key: typing.Hashable, value: typing.Any) -> None:
        key_hash = hash(key) % self.size

        if not self.storage[key_hash]:
            self.storage[key_hash] = HashTableItem(key, value)
        
        else:
            item = self.storage[key_hash]
            
            for item in walk_hashtable_items(item):
                if not item.next:
                    item.next = HashTableItem(key, value)
                    break
                
                if item.key == key:
                    item.value = value
                    break

    def __getitem__(self, key: typing.Hashable) -> typing.Any:
        item = self.__find_item(key)
        
        return item.value
    
    def __contains__(self, key: typing.Hashable) -> bool:
        try:
            self.__find_item(key)
            return True
        
        except KeyError:
            return False
    
    def __delitem__(self, key: typing.Hashable) -> None:
        key_hash = hash(key) % self.size

        if (item := self.storage[key_hash]):
            for item in walk_hashtable_items(item):
                if not item:
                    break
                
                if item.key == key:
                    self.storage[key_hash] = None
                    return
                
                if not item.next:
                    break

                if item.next.key == key:
                    item.next = item.next.next
                    return

        raise KeyError(key)

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
