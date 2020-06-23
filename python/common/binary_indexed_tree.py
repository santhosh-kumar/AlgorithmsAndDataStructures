"""
This module defines the binary indexed tree data structure

We have an array arr[0 . . . n-1]. We would like to
1 Compute the sum of the first i elements.
2 Modify the value of a specified element of the array arr[i] = x where 0 <= i <= n-1.

Binary Indexed Tree achieves O(logn) time complexity for both operations.
"""


class BinaryIndexedTree:
    """
    An implementation of Binary Indexed Tree.
    """

    def __init__(self, input_array):
        """init BITTree
        Args:

        Returns:
            None

        Raises:
            None
        """
        self.bit_tree = [0] * (len(input_array) + 1)

        for i in range(len(input_array)):
            self.update(i, input_array[i], len(input_array))

    def update(self, index, value, length):
        """Update the BitTree

        The idea is based on the fact that all positive integers can be represented as the sum of powers of 2.
        For example 19 can be represented as 16 + 2 + 1. Every node of the BITree stores the sum of n elements where n is a power of 2.
        The number of set bits in the binary representation of a number n is O(Logn).
        Therefore, we traverse at-most O(Logn) nodes in both getSum() and update() operations.
        The time complexity of the construction is O(nLogn) as it calls update() for all n elements.

        Args:
            index: Index of the array element
            value: Value of the array element
            length: Length of the array

        Returns:
            None

        Raises:
            None
        """
        # index in bit_tree[] is 1 more than the index in input_array
        index += 1

        # Traverse all ancestors and add 'val'
        while index <= length:
            # Add 'val' to current node of BI Tree
            self.bit_tree[index] = self.bit_tree[index] + value

            # Update index to that of parent in update View
            # 1) Get 2's complement of the number
            # 2) And it with the original number
            # 3) Add to the original number
            index += index & (-index)

    def get_sum(self, index):
        """get_sum

        Args:
            index: up to which to get sum

        Returns:
            None

        Raises:
            None
        """
        total_sum = 0  # initialize result

        # index in BITree[] is 1 more than the index in arr[]
        index = index + 1

        # Traverse ancestors of BITree[index]
        while index > 0:
            # Add current element of BITree to sum
            total_sum += self.bit_tree[index]

            # Move index to parent node in get_sum View
            # 1) Get 2's complement of the number
            # 2) And it with the original number
            # 3) Subtract from the original number
            # for example, from 7 (111), 2's complement = 000, 2's complement+1 = 001, Subtracting 111-001 = 110.
            # It's essentially flipping the right most bit.
            index -= index & (-index)

        return total_sum
