from __future__ import annotations

import unittest
import dataclasses
import typing

@dataclasses.dataclass
class HashTableItem:
    key: typing.Hashable
    value: typing.Any
    next: typing.Optional[HashTableItem] = None

HashTableItemGenerator = typing.Generator[HashTableItem, None, None]

def walk_hashtable_items(root: HashTableItem) -> HashTableItemGenerator:
    while root:
        yield root
        root = root.next

class HashTable:
    __slots__ = 'size', 'storage'

    def __init__(self, **kwargs: typing.Any):
        self.size: typing.Final = 101111
        self.storage: list[typing.Optional[HashTableItem]] = [None] * self.size

        for key in kwargs:
            self[key] = kwargs[key]
    
    def get(self, key: typing.Hashable, defaul: typing.Any=None) -> typing.Any:
        try:
            return self[key]
        
        except KeyError:
            return defaul
    
    def pop(self, key: typing.Hashable, defaul: typing.Any=None) -> typing.Any:
        try:
            item = self[key]
            del self[key]

            return item
         
        except KeyError:
            return defaul

    def __getitem__(self, key: typing.Hashable) -> typing.Any:
        key_hash = hash(key) % self.size

        if (item := self.storage[key_hash]):
            for item in walk_hashtable_items(item):
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
            
            for item in walk_hashtable_items(item):
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
        table = HashTable(init_key = 'init_value')
        table['key1'] = 'value1'
        table['key2'] = 'value2'
        table[3] = 'value3'
        table[101] = 'value4'
        
        self.assertEqual(table['init_key'], 'init_value')
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
        self.assertEqual(table.pop(101), 'value4')
        self.assertEqual(table.pop(101), None)

if __name__ == '__main__':
    unittest.main()
