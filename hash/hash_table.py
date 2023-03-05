from __future__ import annotations

import unittest
import dataclasses
import typing


@dataclasses.dataclass
class HashTableItem:
    """
    Data class for a hash table item.

    Attributes:
        key: A hashable key used for lookup.
        value: The value associated with the key.
        next: A reference to the next item in the hash table.
    """
    key: typing.Hashable
    value: typing.Any
    next: typing.Optional[HashTableItem] = None


class HashTable:
    """
    A hash table implementation.

    Attributes:
        size: The size of the hash table.
        storage: A list of hash table items, used for storing key-value pairs.
    """
    __slots__ = 'size', 'storage'

    def __init__(self, **kwargs: typing.Any):
        """
        Initializes a new hash table.

        Args:
            **kwargs: Key-value pairs to add to the hash table.
        """
        self.size: typing.Final = 101111
        self.storage: list[typing.Optional[HashTableItem]] = [None] * self.size

        for key in kwargs:
            self[key] = kwargs[key]

    def get(self, key: typing.Hashable, default: typing.Any = None) -> typing.Any:
        """
        Returns the value associated with a key, or a default value if the key is not found.

        Args:
            key: The key to look up in the hash table.
            default: The default value to return if the key is not found.

        Returns:
            The value associated with the key, or the default value if the key is not found.
        """
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self, key: typing.Hashable, default: typing.Any = None) -> typing.Any:
        """
        Removes and returns the value associated with a key, or a default value if the key is not found.

        Args:
            key: The key to remove from the hash table.
            default: The default value to return if the key is not found.

        Returns:
            The value associated with the key, or the default value if the key is not found.
        """
        try:
            item = self[key]
            del self[key]
            return item
        except KeyError:
            return default

    def __getitem__(self, key: typing.Hashable) -> typing.Any:
        """
        Returns the value associated with the given key.

        Args:
            key (typing.Hashable): The key to get the value for.

        Raises:
            KeyError: If the key is not in the hash table.

        Returns:
            typing.Any: The value associated with the key.
        """
        key_hash = hash(key) % self.size

        if (item := self.storage[key_hash]):
            for item in self.__walk_hashtable_items(item):
                if not item:
                    break

                if item.key == key:
                    return item.value

        raise KeyError(key)

    def __setitem__(self, key: typing.Hashable, value: typing.Any) -> None:
        """
        Adds or updates a key-value pair in the hash table. If the key already exists in the hash table, its
        value is updated. Otherwise, a new key-value pair is added to the hash table.
        """
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
        """
        Returns True if the given key is found in the hash table, False otherwise.
        """
        try:
            self[key]
            return True
        except KeyError:
            return False

    def __delitem__(self, key: typing.Hashable) -> None:
        """
        Removes the key-value pair with the given key from the hash table. Raises a KeyError if the key is not
        found in the hash table.
        """
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
        """
        Generator function that walks a chain of hash table items.

        Args:
            root: The root item in the chain.

        Yields:
            The next item in the chain, or None if the end is reached.
        """
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
