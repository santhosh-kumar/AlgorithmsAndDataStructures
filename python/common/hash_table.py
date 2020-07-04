"""
This module defines a hash table
"""
from hashlib import md5

from common.linked_list import LinkedList
from common.linked_list import Node


class HashTable:
    """
    An implementation of the the hash table.
    """
    DEFAULT_HASH_TABLE_SIZE = 32

    def __init__(self, hash_table_size=DEFAULT_HASH_TABLE_SIZE):
        """Init

        Args:
            hash_table_size: Hash table size

        Returns:
            None

        Raises:
            None
        """
        super().__init__()
        self.hash_table_size = hash_table_size
        self.buckets = [LinkedList() for _ in range(hash_table_size)]
        self.keys = {}

    def set(self, key, value):
        """Sets a key:value

        Args:
            key: Key
            value: Value

        Returns:
            None

        Raises:
            None
        """
        key_hash = self.hash(key)
        self.keys[key] = key_hash

        bucket_linked_list = self.buckets[key_hash]
        node = bucket_linked_list.find({key: value})

        if node is None:
            bucket_linked_list.append(Node({key: value}))
        else:
            node.data.value = value

    def get(self, key):
        """Gets the value for the given key

        Args:
            key: Key

        Returns:
            Object

        Raises:
            None
        """
        bucket_linked_list = self.buckets[self.hash(key)]

        # custom linked_list find
        current_node = bucket_linked_list.head
        while current_node is not None:
            for k in current_node.data:
                if k == key:
                    return current_node.data[k]
            current_node = current_node.next_node

        return None

    def delete(self, key):
        """Delete the key/value for the given key

        Args:
            key: Key

        Returns:
            None

        Raises:
            None
        """
        key_hash = self.hash(key)
        del self.keys[key]

        bucket_linked_list = self.buckets[key_hash]

        # custom linked_list find
        node = None
        current_node = bucket_linked_list.head
        while current_node is None and node is None:
            for k in current_node.data:
                if k == key:
                    node = current_node
                    break
            current_node = current_node.next

        if node is not None:
            return bucket_linked_list.delete(node.data)

        return None

    def hash(self, key):
        """Returns the hash from the key

        Args:
            key: to be hashed

        Returns:
            integer

        Raises:
            None
        """
        k = 0
        for s in list(md5(str(key).encode('utf-8')).hexdigest()):
            k += ord(s)
        return k % self.hash_table_size

    def has(self, key):
        """Returns true if the key is in the hash table

        Args:
            key: to be checked

        Returns:
            boolean

        Raises:
            None
        """
        return key in self.keys

    def get_keys(self):
        """Returns the currently stored keys

        Args:

        Returns:
            list

        Raises:
            None
        """
        return self.keys
