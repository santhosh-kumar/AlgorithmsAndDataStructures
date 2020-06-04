"""
Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer that
could point to any node in the list or null.

Return a deep copy of the list
"""
from common.linked_list import LinkedList
from common.linked_list import Node
from common.problem import Problem


class RandomNode(Node):
    """
    An element (node) in the linked list with a random pointer
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
        super().__init__(data)
        self.random = None


class CopyListWithRandomPointer(Problem):
    """
    Copy List with Random Pointer
    """
    PROBLEM_NAME = "CopyListWithRandomPointer"

    def __init__(self, input_linked_list):
        """Copy List with Random Pointer

        Args:
            input_linked_list: linked list
        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_linked_list = input_linked_list

    def solve(self):
        """Solve the problem
            Note: O(n) (runtime) and O(1) (space) solution works by:
             i. Inserting a clone node between two nodes.
             ii. Updating the random pointer of the cloned nodes.
             iii. Detaching original and cloned nodes.

        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        # i. Insert cloned node between two nodes for all the nodes
        current_node = self.input_linked_list.head
        while current_node is not None:
            next_node = current_node.next_node
            new_node = Node(current_node.data)
            current_node.next_node = new_node
            new_node.next_node = next_node
            current_node = next_node

        # ii. Update the random pointer of the cloned node using the random pointer's clone of the original node.
        current_node = self.input_linked_list.head
        while current_node is not None:
            new_node = current_node.next_node
            new_node.random = current_node.random.next_node
            current_node = current_node.next_node.next_node

        # iii. Detach original and cloned nodes
        current_node = self.input_linked_list.head
        cloned_node = current_node.next_node
        while current_node is not None:
            tmp = current_node.next_node
            if current_node.next_node is not None:
                current_node.next_node = current_node.next_node.next_node
            current_node = tmp

        return LinkedList(cloned_node).output_list()
