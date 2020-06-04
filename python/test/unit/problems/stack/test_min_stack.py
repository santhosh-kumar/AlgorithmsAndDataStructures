"""
Unit Test for min_stack
"""
from unittest import TestCase

from problems.stack.min_stack import MinStack


class TestMinStack(TestCase):
    """
    Unit test for MinStack
    """

    def test_get_min(self):
        """Test solve

        Args:
            self: TestMinStack

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [1, 4, 3, 0, 3]
        min_stack = MinStack()
        for i in input_list:
            min_stack.push(i)

        # Then
        # pop 3
        self.assertEqual(min_stack.top(), 3)
        self.assertEqual(min_stack.get_min(), 0)
        self.assertEqual(min_stack.pop(), 3)

        # pop 0
        self.assertEqual(min_stack.top(), 0)
        self.assertEqual(min_stack.get_min(), 0)
        self.assertEqual(min_stack.pop(), 0)

        # pop 3
        self.assertEqual(min_stack.top(), 3)
        self.assertEqual(min_stack.get_min(), 1)
        self.assertEqual(min_stack.pop(), 3)

        # pop 4
        self.assertEqual(min_stack.top(), 4)
        self.assertEqual(min_stack.get_min(), 1)
        self.assertEqual(min_stack.pop(), 4)

        # pop 1
        self.assertEqual(min_stack.top(), 1)
        self.assertEqual(min_stack.get_min(), 1)
        self.assertEqual(min_stack.pop(), 1)

        self.assertIsNone(min_stack.get_min())
