"""
Check if the given array represents a pre-order binary tree.

Input:  pre[] = {2, 4, 3}
Output: true

Given array can represent pre-order traversal
of below tree
    2
     \
      4
     /
    3


Input:  pre[] = {2, 4, 1}
Output: false
Given array cannot represent pre-order traversal
of a Binary Search Tree.
    2
     \
      4
       \
        1


"""
import sys

from common.problem import Problem
from common.stack import Stack


class CheckArrayIsPreOrderBST(Problem):
    """
    Check if the given array represents a pre-order binary tree.
    """
    PROBLEM_NAME = "CheckArrayIsPreOrderBST"

    def __init__(self, input_list):
        """CheckArrayIsPreOrderBST

        Args:
            input_list: Contains an array of numbers

        Returns:
            None

        Raises:
            None
        """
        assert (len(input_list) > 0)

        super().__init__(self.PROBLEM_NAME)
        self.input_list = input_list

    def solve(self):
        """Solve the problem

        Note: O(n logn) (runtime) and O(n) (Space) works by using a stack to store the elements in the order.
        Then, when the right subtree element is reached, it will pop the left subtree elements and then the root is
        set.

        Args:

        Returns:
            boolean

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        value_stack = Stack()

        root = -sys.maxsize

        for value in self.input_list:
            # If we find a node who is on the right side
            # and smaller than root, return False
            if value < root:
                return False

            while len(value_stack) > 0 and value_stack.peek() < value:
                root = value_stack.pop()

            # If we find a node who is on the right side
            # and greater than root, add to the stack
            value_stack.push(value)

        return True
