"""
This module defines linked_list
"""
from abc import ABCMeta, abstractmethod


class BaseLinkedList:
    """
    Abstraction for LinkedList
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def append(self, node):
        """appends a node to the linked list

        Args:
            node: to be appended
        Raises:
        None
        """
        raise NotImplementedError

    @abstractmethod
    def output_list(self):
        """Outputs the linked list

        Args:

        Raises:
        None
        """
        raise NotImplementedError


class Node:
    """
    An element (node) in the linked list
    """

    def __init__(self, data):
        """Init

        Args:
            data: Value of the node

        Returns:
            None

        Raises:
            None
        """
        super().__init__()
        self.data = data
        self.next_node = None

    def __lt__(self, other):
        """Overrides the less than function for heap comparison

        Args:
            other: other node

        Returns:
            boolean

        Raises:
            None
        """
        return self.data < other.data


class BinaryTreeNode:
    """
    An element (node) in a binary tree.
    """

    def __init__(self, data):
        """Init

        Args:
            data: Value of the node

        Returns:
            None

        Raises:
            None
        """
        super().__init__()
        self.data = data
        self.left = None
        self.right = None

    @staticmethod
    def in_order(node, elements_list):
        """Traverse the tree in order with O(n) complexity.

        Args:
            node: currently visited node
            elements_list: List to append values

        Returns:
            elements_list - in_order result

        Raises:
            None
        """
        if node is not None:
            BinaryTreeNode.in_order(node.left, elements_list)
            elements_list.append(node.data)
            BinaryTreeNode.in_order(node.right, elements_list)

    @staticmethod
    def pre_order(node, elements_list):
        """Traverse the tree in pre-order with O(n) complexity

        Args:
            node: currently visited node
            elements_list: List to append values

        Returns:
            elements_list - pre_order result

        Raises:
            None
        """
        if node is not None:
            elements_list.append(node.data)
            BinaryTreeNode.pre_order(node.left, elements_list)
            BinaryTreeNode.pre_order(node.right, elements_list)

    @staticmethod
    def post_order(node, elements_list):
        """Traverse the tree in pre-order with O(n) complexity

        Args:
            node: currently visited node
            elements_list: List to append values

        Returns:
            elements_list - post_order result

        Raises:
            None
        """
        if node is not None:
            BinaryTreeNode.post_order(node.left, elements_list)
            BinaryTreeNode.post_order(node.right, elements_list)
            elements_list.append(node.data)


class LinkedList(BaseLinkedList):
    """
    Concrete implementation of LinkedList
    """

    def __init__(self, head=None):
        """Init

        Args:

        Returns:
            None

        Raises:
            None
        """
        super().__init__()
        self.head = head

    def append(self, node):
        """appends a node to the end of the linked list

        Args:
            node: to be appended
        Raises:
        None
        """
        if self.head is None:
            self.head = node
        else:
            last_node = self.head
            while last_node.next_node is not None:
                last_node = last_node.next_node

            last_node.next_node = node

    def output_list(self):
        """Outputs the linked list

        Args:

        Returns:
            Linked list as a list of integers

        Raises:
        None
        """
        output_list = []
        if self.head is not None:
            last_node = self.head
            while last_node.next_node is not None:
                output_list.append(last_node.data)
                last_node = last_node.next_node
            output_list.append(last_node.data)

        return output_list
