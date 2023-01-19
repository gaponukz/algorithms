import unittest

class SparseList(list):
    def __setitem__(self, index, value):
        sparsity = index - len(self) + 1
        self.extend([None] * sparsity)
        list.__setitem__(self, index, value)

class HashTable(object):
    def __init__(self, size=9973):
        self.size = size
        self.storage = SparseList()
        self.storage = [None] * size

    def __setitem__(self, key, value):
        key_hash = hash(key) % self.size

        if not self.storage[key_hash]:
            self.storage[key_hash] = [ [key, value] ].copy()
        
        else:
            for index in range(len(self.storage[key_hash])):
                if self.storage[key_hash][index][0] == key:
                    self.storage[key_hash][index][1] = value
                    return

            self.storage[key_hash].append([key, value])

    def __getitem__(self, key):
        key_hash = hash(key) % self.size

        if self.storage[key_hash]:
            for index in range(len(self.storage[key_hash])):
                if self.storage[key_hash][index][0] == key:
                    return self.storage[key_hash][index][1]

        raise KeyError(key)
    
    def __contains__(self, key):
        try:
            return self[key] != None
        
        except KeyError:
            return False

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

if __name__ == '__main__':
    unittest.main()
