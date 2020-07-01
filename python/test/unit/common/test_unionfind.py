"""
Unit Test for unionfind
"""
from unittest import TestCase

from common.union_find import UnionFind


class TestUnionFind(TestCase):
    """
    Unit test for UnionFind
    """

    def test_union_find(self):
        """Test for union & find

        Args:
            self: TestUnionFind

        Returns:
            None

        Raises:
            None
        """
        # Given
        n = 10
        data = [i for i in range(n)]
        adjacency_list = [(0, 1), (1, 2), (0, 9), (5, 6), (6, 4), (5, 9)]
        union_find = UnionFind(data)

        # When
        for i, j in adjacency_list:
            union_find.union(i, j)

        # Then
        self.assertEqual(union_find.find(0), 9)
        self.assertEqual(union_find.find(1), 9)
        self.assertEqual(union_find.find(2), 9)
        self.assertEqual(union_find.find(3), 3)
        self.assertEqual(union_find.find(4), 9)
        self.assertEqual(union_find.find(5), 9)
        self.assertEqual(union_find.find(6), 9)
        self.assertEqual(union_find.find(7), 7)
        self.assertEqual(union_find.find(8), 8)
        self.assertEqual(union_find.find(9), 9)
