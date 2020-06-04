"""
Binary Tree Max Sum Path

Given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.

For example, given the below binary tree:

         1
        / \
       2   4
      / \
    2    3

4 -> 1 -> 2-> 3 is the maximum sum path (10).

Example Questions Candidate Might Ask:
Q: What if the tree is empty?
A: Assume the tree is non-empty.

Q: How about a tree that contains only a single node?
A: Then the maximum path sum starts and ends at the same node.

Q: What if every node contains negative value?
A: Then you should return the single node value that is the least negative.

Q: Does the maximum path have to go through the root node?
A: Not necessarily. For example, the below tree yield 6 as the maximum path sum and does not
go through root.
    -5
    / \
   2   3
  / \
-1   4
"""
from common.problem import Problem


class BinaryTreeMaxSumPath(Problem):
    """
    Binary Tree Max Sum Path
    """
    PROBLEM_NAME = "BinaryTreeMaxSumPath"
    MIN_INT_VALUE = -2147483647

    def __init__(self, root_node):
        """Binary Tree Max Sum Path

        Args:
            root_node: node of the tree

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.root_node = root_node
        self.max_sum = self.MIN_INT_VALUE

    def solve(self):
        """Solve the problem
            Note: For the bottom up approach. At each node, the potential maximum path could be one of these cases:
            i. max(left subtree) + node
            ii. max(right subtree) + node
            iii. max(left subtree) + max(right subtree) + node
            iv. the node itself

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        self.find_max(self.root_node)
        return self.max_sum

    def find_max(self, node):
        """Find the max

        Args:
            node: root node

        Returns:
            integer

        Raises:
            None
        """
        if node is None:
            return 0

        left_max = self.find_max(node.left)
        right_max = self.find_max(node.right)

        self.max_sum = max(node.data + left_max + right_max, self.max_sum)

        return_value = node.data + max(left_max, right_max)

        if return_value > 0:
            return return_value
        else:
            return 0
