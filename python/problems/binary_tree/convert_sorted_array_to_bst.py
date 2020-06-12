"""
Convert Sorted Array to a Balanced Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height
balanced BST.
"""
from common.linked_list import BinaryTreeNode
from common.problem import Problem


class ConvertSortedArrayToBST(Problem):
    """
    Convert Sorted Array to a Balanced Binary Search Tree
    """
    PROBLEM_NAME = "ConvertSortedArrayToBST"

    def __init__(self, input_list):
        """Convert Sorted Array to a Balanced Binary Search Tree

        Args:
            input_list: Contains a sorted list of integers

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

        Note: O(n) (runtime) and O(log n) space works with the divide and conquer methodology.

        Args:

        Returns:
            None

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        return self.sorted_array_to_bst(self.input_list, 0, len(self.input_list) - 1)

    def sorted_array_to_bst(self, number_list, start, end):
        """Convert sorted array to Binary Search Tree

        Args:
            number_list: input list
            start: start index
            end: end index

        Returns:
            BinaryTreeNode

        Raises:
            None
        """
        if start > end:
            return None

        middle = int((start + end) / 2)

        node = BinaryTreeNode(number_list[middle])
        node.left = self.sorted_array_to_bst(number_list, start, middle - 1)
        node.right = self.sorted_array_to_bst(number_list, middle + 1, end)

        return node
