"""
This module defines the segment tree data structure

Let us consider the following problem to understand Segment Trees without recursion.

We have an array arr[0 . . . n-1]. We should be able to,

Find the sum of elements from index l to r where 0 <= l <= r <= n-1
Change value of a specified element of the array to a new value x. We need to do arr[i] = x where 0 <= i <= n-1.

Time Complexities:

Tree Construction : O( n )
Query in Range : O( Log n )
Updating an element : O( Log n )
"""


class SegmentTree:
    """
    An implementation of Segment Tree
    """

    MAX_ARRAY_SIZE = 100

    def __init__(self, input_array):
        """init Segment Tree
        Args:
            input_array: Input array

        Returns:
            None

        Raises:
            None
        """
        self.tree = [0] * (2 * self.MAX_ARRAY_SIZE)

        # insert lead nodes in the tree
        n = len(input_array)
        self.n = n
        for i in range(n):
            self.tree[n + i] = input_array[i]

        # build the tree by calculating parents
        for i in range(n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, index, value):
        """Update

        Args:
            index: to update
            value: new value

        Returns:
            None

        Raises:
            None
        """
        # set value at position p
        self.tree[index + self.n] = value
        index = index + self.n

        # move upward and update parents
        i = index
        while i > 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1

    def query(self, left_index, right_index):
        """Query range

        Args:
            left_index: start index
            right_index: end index

        Returns:
            None

        Raises:
            None
        """
        result = 0

        # loop to find the sum in the range
        left_index += self.n
        right_index += self.n

        while left_index < right_index:
            if left_index & 1:
                result += self.tree[left_index]
                left_index += 1

            if right_index & 1:
                right_index -= 1
                result += self.tree[right_index]

            left_index >>= 1
            right_index >>= 1

        return result
