"""
This module defines linked_list
"""


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


class LinkedList:
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

    def find(self, data):
        """Find the node with the given data

        Args:
            data: to be found

        Return:
            Node

        Raises:
            None
        """
        current_node = self.head

        while current_node is not None:
            if current_node.data == data:
                return current_node
            current_node = current_node.next_node

        return None

    def delete(self, data):
        """Delete the node with the given data

        Args:
            data: to be found

        Return:
            Node

        Raises:
            None
        """
        current_node = self.head

        if current_node is None:
            return

        previous_node = None
        while current_node is not None:
            if current_node.data == data:
                break
            previous_node = current_node
            current_node = current_node.next_node

        if previous_node is not None:
            previous_node.next_node = current_node.next_node

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
