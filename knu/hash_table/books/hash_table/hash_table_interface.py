import typing
import abc

class IHashTable(abc.ABC):
    """ A hash table implementation. """

    def __init__(self, **kwargs: typing.Any):
        """
        Initializes a new hash table.

        Args:
            **kwargs: Key-value pairs to add to the hash table.
        """
        pass
    
    def get(self, key: typing.Hashable, default: typing.Any = None) -> typing.Any:
        """
        Returns the value associated with a key, or a default value if the key is not found.

        Args:
            key: The key to look up in the hash table.
            default: The default value to return if the key is not found.

        Returns:
            The value associated with the key, or the default value if the key is not found.
        """
        pass

    def pop(self, key: typing.Hashable, default: typing.Any = None) -> typing.Any:
        """
        Removes and returns the value associated with a key, or a default value if the key is not found.

        Args:
            key: The key to remove from the hash table.
            default: The default value to return if the key is not found.

        Returns:
            The value associated with the key, or the default value if the key is not found.
        """
        pass
    
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
        pass
    
    def __setitem__(self, key: typing.Hashable, value: typing.Any) -> None:
        """
        Adds or updates a key-value pair in the hash table. If the key already exists in the hash table, its
        value is updated. Otherwise, a new key-value pair is added to the hash table.
        """
        pass

    def __contains__(self, key: typing.Hashable) -> bool:
        """
        Returns True if the given key is found in the hash table, False otherwise.
        """
        pass

    def __delitem__(self, key: typing.Hashable) -> None:
        """
        Removes the key-value pair with the given key from the hash table. Raises a KeyError if the key is not
        found in the hash table.
        """
        pass
