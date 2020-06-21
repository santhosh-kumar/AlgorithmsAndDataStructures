"""
Reverse a Linked List for a given group size

Given a linked list, write a function to reverse every k nodes (where k is an input to the function).

Examples:

Inputs:  1->2->3->4->5->6->7->8->NULL and k = 3
Output:  3->2->1->6->5->4->8->7->NULL.

Inputs:   1->2->3->4->5->6->7->8->NULL and k = 5
Output:  5->4->3->2->1->8->7->6->NULL.
"""
from common.problem import Problem
from common.stack import Stack


class ReverseLinkedListWithGroupSize(Problem):
    """
    Reverse Linked List for a Given Group Size
    """
    PROBLEM_NAME = "ReverseLinkedListWithGroupSize"

    def __init__(self, input_linked_list, group_size):
        """Reverse Linked List for a Given Group Size

        Args:
            input_linked_list: to reverse
            group_size: size

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_linked_list = input_linked_list
        self.group_size = group_size

    def solve(self):
        """Solve the problem

        Note:

        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        current_node = self.input_linked_list.head
        previous_node = None

        count = 0
        group_stack = Stack()

        # append the nodes to the stack till the required group size
        while current_node is not None and count < self.group_size:
            group_stack.push(current_node)
            current_node = current_node.next_node
            count = count + 1

        # pop nodes from the stack and re-point the head
        while len(group_stack) > 0:
            if previous_node is None:
                previous_node = group_stack.pop()
                self.input_linked_list.head = previous_node
            else:
                previous_node.next_node = group_stack.pop()
                previous_node = previous_node.next_node

        previous_node.next_node = current_node

        return self.input_linked_list.output_list()
