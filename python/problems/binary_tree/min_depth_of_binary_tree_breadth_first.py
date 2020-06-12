"""
Min Depth of Binary Tree (Breadth First)

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""
from collections import deque

from common.problem import Problem


class MinDepthOfBinaryTreeBreadthFirst(Problem):
    """
    Min Depth of Binary Tree (Breadth First)
    """
    PROBLEM_NAME = "MinDepthOfBinaryTreeBreadthFirst"

    def __init__(self, root_node):
        """Min Depth of Binary Tree (Breadth First)

        Args:
            root_node: node of the tree

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.root_node = root_node

    def solve(self):
        """Solve the problem

        Note: Depth first traverses all the nodes even for a highly un-balanced tree. However, breadth first stops
        traversing when we first encounter the first leaf node. The complexity O(n) (runtime) and O(n) (space).
        The worst case complexity happens when the binary tree has n nodes and it's balanced. The space complexity of
        O(n) happens due to storing the elements in a queue.

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        return self.min_depth(self.root_node)

    @staticmethod
    def min_depth(root):
        """Find the minimum depth of a binary tree

        Args:
            root: node of the tree

        Returns:
            None

        Raises:
            None
        """
        if root is None:
            return 0

        nodes_queue = deque()
        nodes_queue.append(root)

        right_most_node = root
        depth = 1

        while len(nodes_queue) > 0:
            node = nodes_queue.popleft()

            if node.left is None and node.right is None:
                break

            if node.left is not None:
                nodes_queue.append(node.left)

            if node.right is not None:
                nodes_queue.append(node.right)

            if node == right_most_node:
                depth = depth + 1

                if node.right is not None:
                    right_most_node = node.right
                else:
                    right_most_node = node.left

        return depth
