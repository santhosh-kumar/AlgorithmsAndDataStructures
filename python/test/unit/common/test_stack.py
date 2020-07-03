"""
Unit Test for stack
"""
from unittest import TestCase

from common.stack import Stack


class TestStack(TestCase):
    """
    Unit test for Stack
    """

    def test_stack(self):
        """Test for get_orientation

        Args:
            self: TestStack

        Returns:
            None

        Raises:
            None
        """
        # Given
        n = 4
        stack = Stack()
        for i in range(n):
            stack.push(i)

        # Then
        self.assertEqual(len(stack), n)
        for i in reversed(range(len(stack))):
            self.assertEqual(stack.pop(), i)
