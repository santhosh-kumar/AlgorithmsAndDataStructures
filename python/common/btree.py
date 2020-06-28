"""
This module defines the BTree data structure

B-Tree is a m-way search tree with the following properties:

1) All leaves are at the same level.
2) A B-Tree is defined by the term minimum degree ‘t’. The value of t depends upon disk block size.
3) Every node except root must contain at least t-1 keys. The root may contain minimum 1 key.
4) All nodes (including root) may contain at most 2t – 1 keys.
5) Number of children of a node is equal to the number of keys in it plus 1.
6) All keys of a node are sorted in increasing order. The child between two keys k1 and k2 contains all keys in the range from k1 and k2.
7) B-Tree grows and shrinks from the root which is unlike Binary Search Tree. Binary Search Trees grow downward and also shrink from downward.
8) Like other balanced Binary Search Trees, time complexity to search, insert and delete is O(log n).
"""


class BTreeNode:
    """
    A node in BTree
    """

    def __init__(self, is_leaf=False):
        """init BTreeNode
        Args:
            is_leaf: If the node is the leaf node

        Returns:
            None

        Raises:
            None
        """
        self.is_leaf = is_leaf
        self.keys = []
        self.children = []

    def __str__(self):
        """__str__
        Args:

        Returns:
            string

        Raises:
            None
        """
        if self.is_leaf:
            return "Leaf BTreeNode with {0} keys\n\tK:{1}\n\tC:{2}\n".format(len(self.keys), self.keys, self.children)
        else:
            return "Internal BTreeNode with {0} keys, {1} children\n\tK:{2}\n\n".format(len(self.keys),
                                                                                        len(self.children), self.keys,
                                                                                        self.children)


class BTree:
    """
    An implementation of BTree
    """
    NOT_FOUND = -1

    def __init__(self, min_degree):
        """init BTree
        Args:
            min_degree: min degree of the node

        Returns:
            None

        Raises:
            None
        """
        self.root = BTreeNode(is_leaf=True)
        self.min_degree = min_degree  # (2 * min_degree - 1) keys allowed

    def search(self, key, node=None):
        """Search for a value from the starting node

        Args:
            key: to search
            node: Node to start with

        Returns:
            BTreeNode, integer

        Raises:
            None
        """
        if isinstance(node, BTreeNode):
            i = 0

            # look for index of k
            while i < len(node.keys) and key > node.keys[i]:
                i += 1

            # found exact match
            if i < len(node.keys) and key == node.keys[i]:
                return node, i
            # no match in keys, and is leaf ==> no match exists
            elif node.is_leaf:
                return None, self.NOT_FOUND
            # search children
            else:
                return self.search(key, node.children[i])
        else:
            return self.search(key, self.root)

    def insert(self, key):
        """Insert a key

        Args:
            key: to insert

        Returns:
            None

        Raises:
            None
        """
        r = self.root

        # keys are full, so we must split
        if len(r.keys) == (2 * self.min_degree) - 1:
            s = BTreeNode()
            self.root = s

            # former root is now 0th child of new root s
            s.children.insert(0, r)

            # Split the child from the new root
            self._split_child(s, 0)

            self._insert_nonfull(s, key)
        else:
            self._insert_nonfull(r, key)

    def _split_child(self, node, index):
        """Split a node

        Args:
            node:
            index:

        Returns:
            None

        Raises:
            None
        """
        min_degree = self.min_degree

        y = node.children[index]
        z = BTreeNode(is_leaf=y.is_leaf)

        # slide all children of node to the right and insert z at i+1.
        node.children.insert(index + 1, z)
        node.keys.insert(index, y.keys[min_degree - 1])

        # keys of z are t to 2t - 1,
        # y is then 0 to t-2
        z.keys = y.keys[min_degree:(2 * min_degree - 1)]
        y.keys = y.keys[0:(min_degree - 1)]

        # children of z are min_degree to 2 * min_degree else of y.children
        if not y.is_leaf:
            z.children = y.children[min_degree:(2 * min_degree)]
            y.children = y.children[0:min_degree]

    def _insert_nonfull(self, node, key):
        """Insert a key

        Args:
            node: to insert the key
            key: to insert

        Returns:
            None

        Raises:
            None
        """
        i = len(node.keys) - 1

        if node.is_leaf:
            # insert a key
            node.keys.append(0)

            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1

            node.keys[i + 1] = key
        else:
            # insert a child
            while i >= 0 and key < node.keys[i]:
                i -= 1

            i += 1
            if len(node.children[i].keys) == (2 * self.min_degree) - 1:
                self._split_child(node, i)

                if key > node.keys[i]:
                    i += 1

            self._insert_nonfull(node.children[i], key)

    def __str__(self):
        """__str__
        Args:

        Returns:
            string

        Raises:
            None
        """
        r = self.root
        return r.__str__() + '\n'.join([child.__str__() for child in r.children])
