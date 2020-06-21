"""
Find Lowest Common Ancestor in a Binary Tree

Given a binary tree (not a binary search tree) and two values say n1 and n2, write a program to find the least common ancestor.

"""
from common.problem import Problem


class FindLowestCommonAncestor(Problem):
    """
    Find Lowest Common Ancestor
    """
    PROBLEM_NAME = "FindLowestCommonAncestor"

    def __init__(self, root_node, label1, label2):
        """Find Lowest Common Ancestor

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

        Note:

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        return self.find_lca(self.root_node, self.label1, self.label2)

    def find_lca(self, root, label1, label2):
        """Find the lowest common ancestor

        Args:
            root: root node of the tree
            label1: First node's label
            label2: Second node's label

        Returns:
            BinaryTreeNode

        Raises:
            None
        """
        # Base case
        if root is None:
            return None

        # If either n1 or n2 matches with root's key, report
        # the presence by returning root (Note that if a key is
        # ancestor of other, then the ancestor key becomes LCA
        if root.data == label1 or root.data == label2:
            return root

        # Look for keys in left and right subtrees
        left_lca = self.find_lca(root.left, label1, label2)
        right_lca = self.find_lca(root.right, label1, label2)

        # If both of the above calls return Non-NULL, then one key
        # is present in once subtree and other is present in other,
        # So this node is the LCA
        if left_lca and right_lca:
            return root

        # Otherwise check if left subtree or right subtree is LCA
        if left_lca is not None:
            return left_lca
        elif right_lca is not None:
            return right_lca
        else:
            return None
