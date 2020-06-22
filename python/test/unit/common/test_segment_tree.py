"""
Unit Test for segment_tree
"""
from unittest import TestCase

from common.segment_tree import SegmentTree


class TestSegmentTree(TestCase):
    """
    Unit test for SegmentTree
    """

    def test_segment_tree(self):
        """Test for update and query

        Args:
            self: TestSegmentTree

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        segment_tree = SegmentTree(input_array)

        # Then
        for i in range(len(input_array)):
            total_sum = (i * (i + 1) / 2)
            self.assertEqual(segment_tree.query(0, i), total_sum)
