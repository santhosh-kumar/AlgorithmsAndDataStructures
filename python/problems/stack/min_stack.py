"""
Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in
constant time.

 push(x) – Push element x onto stack.
 pop() – Removes the element on top of the stack.
 top() – Get the top element.
 getMin() – Retrieve the minimum element in the stack.

Hints:
 Consider space-time trade-off. How would you keep track of the minimums using
extra space?

 Make sure to consider duplicate elements.
"""
from common.problem import Problem
from common.stack import Stack


class MinStack(Problem):
    """
    Min Stack
    """
    PROBLEM_NAME = "MinStack"

    def __init__(self):
        """Min Stack

        Args:

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_stack = Stack()
        self.min_stack = Stack()

    def solve(self):
        """Solve the problem

        Args:

        Returns:
            None

        Raises:
            None
        """
        pass

    def push(self, data):
        """Push an element to the stack

        Args:

        Returns:
            None

        Raises:
            None
        """
        self.input_stack.push(data)

        if self.min_stack.peek() is None or data < self.min_stack.peek():
            self.min_stack.push(data)

    def pop(self):
        """Pops the element from the stack

        Args:

        Returns:
            data

        Raises:
            None
        """
        data = self.input_stack.pop()

        if data == self.min_stack.peek():
            self.min_stack.pop()

        return data

    def top(self):
        """Return the top element from the input stack

        Args:

        Returns:
            data

        Raises:
            None
        """
        return self.input_stack.peek()

    def get_min(self):
        """Return the min element from the min stack

        Args:

        Returns:
            data

        Raises:
            None
        """
        return self.min_stack.peek()
