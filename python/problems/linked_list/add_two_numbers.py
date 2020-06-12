"""
Add Two Numbers

You are given two linked lists representing two non-negative numbers. The digits are
stored in reverse order and each of their nodes contains a single digit. Add the two
numbers and return it as a linked list.

Input: (2  4  3) + (5  6  4)
Output: 7  0  8

"""
from common.linked_list import LinkedList
from common.linked_list import Node
from common.problem import Problem


class AddTwoNumbers(Problem):
    """
    Add Two Numbers
    """
    PROBLEM_NAME = "AddTwoNumbers"

    def __init__(self, input_linked_list1, input_linked_list2):
        """Add Two Numbers

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

        Note: O(n) (runtime) solution works by simultaneously iterating over both the list and taking the carry to the digit.

        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        node1 = self.input_linked_list1.head
        node2 = self.input_linked_list2.head

        carry = 0
        sum_list = LinkedList()
        while node1 is not None and node2 is not None:
            digit1 = node1.data
            digit2 = node2.data

            digit_sum = digit1 + digit2 + carry

            if digit_sum > 9:
                carry = 1
            else:
                carry = 0

            sum_list.append(Node(digit_sum % 10))

            node1 = node1.next_node
            node2 = node2.next_node

        node = None
        if node1 is None and node2 is not None:
            node = node2
        elif node1 is not None and node2 is None:
            node = node1

        while node is not None:
            digit_sum = node.data + carry
            if digit_sum > 9:
                carry = 1
            sum_list.append(Node(digit_sum % 10))
            node = node.next_node

        return list(reversed(sum_list.output_list()))
