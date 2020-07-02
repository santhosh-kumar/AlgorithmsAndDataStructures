"""
This module defines the bloom filter.
"""
import math

import mmh3
from bitarray import bitarray


class BloomFilter:
    """
    Class for Bloom filter, using murmur3 hash function
    """

    def __init__(self, items_count, false_positives_prob):
        """Init

        Args:
            items_count: Number of items expected to be stored in the bloom filter
            false_positives_prob: False Positive probability in decimal

        Returns:
            None

        Raises:
            None
        """
        self.false_positives_prob = false_positives_prob
        self.size = self.get_size(items_count, false_positives_prob)
        self.hash_count = self.get_hash_count(self.size, items_count)
        self.bit_array = bitarray(self.size)

    @classmethod
    def get_size(cls, n, p):
        """
        Return the size of bit array(m) to used using following formula
        m = -(n * lg(p)) / (lg(2)^2)

        Args:
            n : number of items expected to be stored in filter
            p : False Positive probability in decimal

        Returns:
            integer

        Raises:
            None
        """
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    @classmethod
    def get_hash_count(cls, m, n):
        """
        Return the hash function(k) to be used using following formula
        k = (m/n) * lg(2)

        Args:
            m : size of bit array
            n : number of items expected to be stored in filter
        """
        k = (m / n) * math.log(2)
        return int(k)

    def add(self, item):
        """
        Add an item in the filter

        Args:
            item: to add in the filter

        Returns:
            None

        Raises:
            None
        """
        digests = []
        for i in range(self.hash_count):
            # create digest for given item.
            # i work as seed to mmh3.hash() function
            # With different seed, digest created is different
            digest = mmh3.hash(item, i) % self.size
            digests.append(digest)

            # set the bit True in bit_array
            self.bit_array[digest] = True

    def check(self, item):
        """
        Check for existence of an item in filter

        Args:
            item: to check in the filter

        Returns:
            boolean

        Raises:
            None
        """
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if not self.bit_array[digest]:
                # if any of bit is False then,its not present
                # in filter
                # else there is probability that it exist
                return False
        return True
