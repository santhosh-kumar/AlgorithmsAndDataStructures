"""
Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1  2  3  4, you should return the list as 2  1  4  3.

Your algorithm should use only constant space. You may not modify the values in the
list, only nodes itself can be changed.

Example Questions Candidate Might Ask:
Q: What if the number of nodes in the linked list has only odd number of nodes?
A: The last node should not be swapped.
"""
from common.problem import Problem


class SwapNodesInPairs(Problem):
    """
    Swap Nodes In Pairs
    """
    PROBLEM_NAME = "SwapNodesInPairs"

    def __init__(self, input_linked_list):
        """Swap Nodes in Pairs

        Args:
            input_linked_list: to swap adjacent nodes
        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_linked_list = input_linked_list

    def solve(self):
        """Solve the problem

        Note: O(n) solution works by comparing adjacent nodes and swapping values.

        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        node1 = self.input_linked_list.head

        while node1 is not None:
            if node1.next_node is not None:
                node2 = node1.next_node

                node1_value = node1.data
                node2_value = node2.data

                node1.data = node2_value
                node2.data = node1_value
                node1 = node2.next_node
            else:
                node1 = None

        return self.input_linked_list.output_list()
