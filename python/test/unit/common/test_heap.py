"""
Unit Test for trie
"""
from unittest import TestCase

from common.heap import MaxHeap
from common.heap import MinHeap


class TestHeap(TestCase):
    """
    Unit test for MaxHeap
    """

    def test_min_heap(self):
        """Test for min heap

        Args:
            self: TestHeap

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [4, 7, 8, 3, 2, 6, 5]
        min_heap = MinHeap(input_list)

        # When
        min_heap.heap_push(1)
        min_heap.heap_push(9)
        min_heap.heap_push(10)

        # Then
        self.assertEqual(min_heap.height(), 4)

        self.assertEqual(min_heap.heap_pop(), 1)
        self.assertEqual(min_heap.heap_pop(), 2)
        self.assertEqual(min_heap.heap_pop(), 3)
        self.assertEqual(min_heap.heap_pop(), 4)
        self.assertEqual(min_heap.heap_pop(), 5)
        self.assertEqual(min_heap.heap_pop(), 6)
        self.assertEqual(min_heap.heap_pop(), 7)
        self.assertEqual(min_heap.heap_pop(), 8)
        self.assertEqual(min_heap.heap_pop(), 9)
        self.assertEqual(min_heap.heap_pop(), 10)

    def test_max_heap(self):
        """Test for max heap

        Args:
            self: TestHeap

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [4, 7, 8, 3, 2, 6, 5]
        max_heap = MaxHeap(input_list)

        # When
        max_heap.heap_push(1)
        max_heap.heap_push(9)
        max_heap.heap_push(10)

        # Then
        self.assertEqual(max_heap.height(), 4)

        self.assertEqual(max_heap.heap_pop(), 10)
        self.assertEqual(max_heap.heap_pop(), 9)
        self.assertEqual(max_heap.heap_pop(), 8)
        self.assertEqual(max_heap.heap_pop(), 7)
        self.assertEqual(max_heap.heap_pop(), 6)
        self.assertEqual(max_heap.heap_pop(), 5)
        self.assertEqual(max_heap.heap_pop(), 4)
        self.assertEqual(max_heap.heap_pop(), 3)
        self.assertEqual(max_heap.heap_pop(), 2)
        self.assertEqual(max_heap.heap_pop(), 1)
