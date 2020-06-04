"""
This module defines the union find data structure (disjoint sets)
"""


class UnionFind:
    """
    An implementation of union find.
    """

    def __init__(self, data_list):
        """init union find
        Args:
            data_list: List of items
        Returns:
            None

        Raises:
            None
        """
        self.data_list = data_list

    def find(self, i):
        """find
        Args:
            i: index of the element

        Returns:
            integer -- parent index

        Raises:
            None
        """
        # if the element is not its own parent
        if i != self.data_list[i]:
            self.data_list[i] = self.find(self.data_list[i])

        return self.data_list[i]

    def union(self, i, j):
        """union
        Args:
            i: index of the first element
            j: index of the second element

        Returns:
            None

        Raises:
            None
        """
        # find the parents of i and j
        pi, pj = self.find(i), self.find(j)

        # if they have different parents, connect them.
        if pi != pj:
            self.data_list[pi] = pj

    def is_connected(self, i, j):
        """Check if connected
        Args:
            i: index of the first element
            j: index of the second element

        Returns:
            boolean

        Raises:
            None
        """
        return self.find(i) == self.find(j)
