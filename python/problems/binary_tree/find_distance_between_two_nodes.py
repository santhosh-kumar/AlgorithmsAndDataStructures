"""
Find the distance between two nodes

Find the distance between two keys in a binary tree, no parent pointers are given.
Distance between two nodes is the minimum number of edges to be traversed to reach one node from other.

"""
from common.problem import Problem


class FindDistanceBetweenTwoNodes(Problem):
    """
    Find Distance Between Two Nodes
    """
    PROBLEM_NAME = "FindDistanceBetweenTwoNodes"

    def __init__(self, root_node, label1, label2):
        """Find Distance Between Two Nodes

        Args:
            root_node: node of the tree
            label1: First node's label
            label2: Second node's label

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.root_node = root_node
        self.label1 = label1
        self.label2 = label2

    def solve(self):
        """Solve the problem

        Note: O(n) (runtime) as the method does a single tree traversal.

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        path1 = []
        self.path_to_node(self.root_node, path1, self.label1)

        path2 = []
        self.path_to_node(self.root_node, path2, self.label2)

        # iterate through the paths to find the
        # common path length
        i = 0
        while i < len(path1) and i < len(path2):
            # get out as soon as the path differs
            # or any path's length get exhausted
            if path1[i] != path2[i]:
                break
            i = i + 1

        # get the path length by deducting the
        # intersecting path length (or till LCA)
        return (len(path1) + len(path2) - 2 * i)

    def path_to_node(self, root, path, node):
        """Find path to node

        Args:
            root: root node of the tree
            path: list of nodes
            node: node for which to find the path

        Returns:


        Raises:
            None
        """
        if root is None:
            return True

        # append the node value in path
        path.append(root.data)

        # See if the node is same as root's data
        if root.data == node:
            return True

        # Check if k is found in left or right sub-tree
        if root.left is not None and self.path_to_node(root.left, path, node):
            return True

        if root.right is not None and self.path_to_node(root.right, path, node):
            return True

        # If not present in subtree rooted with root,
        # remove root from path and return False
        path.pop()
        return False
