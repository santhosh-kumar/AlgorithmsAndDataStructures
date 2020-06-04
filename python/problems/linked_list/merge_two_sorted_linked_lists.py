"""
Merge Two Sorted Linked Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by
splicing together the nodes of the first two list
"""
from common.linked_list import LinkedList
from common.linked_list import Node
from common.problem import Problem


class MergeTwoSortedLinkedLists(Problem):
    """
    Merge Two Sorted Linked Lists
    """
    PROBLEM_NAME = "MergeTwoSortedLinkedLists"

    def __init__(self, input_linked_list1, input_linked_list2):
        """Merge Two Sorted Linked Lists

        Args:
            input_linked_list1: First linked list
            input_linked_list2: Second linked list
        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_linked_list1 = input_linked_list1
        self.input_linked_list2 = input_linked_list2

    def solve(self):
        """Solve the problem

        Note: O(n) (runtime) and O(1) (space) solution works by iterating over both the linked lists
              and appending the smallest one to the merged_list.

        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        merged_list = LinkedList()

        node1 = self.input_linked_list1.head
        node2 = self.input_linked_list2.head

        # iterate over both the lists and append the smallest
        while node1 is not None and node2 is not None:
            if node1.data < node2.data:
                merged_list.append(Node(node1.data))
                node1 = node1.next_node
            else:
                merged_list.append(Node(node2.data))
                node2 = node2.next_node

        # append the remaining elements from the second list
        if node1 is None:
            while node2 is not None:
                merged_list.append(Node(node2.data))
                node2 = node2.next_node

        # append the remaining elements from the first list
        if node2 is None:
            while node1 is not None:
                merged_list.append(Node(node1.data))
                node1 = node1.next_node

        return merged_list.output_list()
