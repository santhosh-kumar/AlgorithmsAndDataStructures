"""
Merge K Sorted Linked Lists Divide and Conquer (Divide and Conquer based solution)

Merge k sorted linked lists and return it as a new list. The new list should be made by
splicing together the nodes of the first two list.
"""
from common.linked_list import LinkedList
from common.linked_list import Node
from common.problem import Problem


class MergeKSortedLinkedListsDivideAndConquer(Problem):
    """
    Merge K Sorted Linked Lists Divide and Conquer
    """
    PROBLEM_NAME = "MergeKSortedLinkedListsDivideAndConquer"

    def __init__(self, input_linked_lists_list):
        """Merge K Sorted Linked Lists Divide and Conquer

        Args:
            input_linked_lists_list: List of linked lists
        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_linked_lists_list = input_linked_lists_list

    def solve(self):
        """Solve the problem
        Note:
            i. Brute force solution would work by comparing two lists at a time for k times. The total runtime complexity would be O(nk^2)
        = 2n + 3n + 4n + ... + kn = n(k(k+1)/2 -1). The solution will only require a constant space O(1).

           ii. Heap has a complexity of O(log k) to order based on the heap property. We could maintain a heap of size k with smallest element from each list.
           After removing a element from the list, the next element is placed in the heap. With nk elements, the overall runtime complexity is O(nk logk) and
           a space complexity of O(k).

           iii. Divide and conquer works by merging two different lists at the same time (begin and end), and finally merging two combined lists.
           Compared to brute force with k merges O(nk^2), the runtime complexity is O(nk logk) and the space complexity of O(1).
        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        if len(self.input_linked_lists_list) == 0:
            return []

        input_linked_lists_list = []
        for k in range(len(self.input_linked_lists_list)):
            input_linked_lists_list.append(self.input_linked_lists_list[k].head)

        end = len(self.input_linked_lists_list) - 1

        while end > 0:
            begin = 0
            while begin < end:
                input_linked_lists_list[begin] = self.merge_two_sorted_linked_lists(input_linked_lists_list[begin],
                                                                                    input_linked_lists_list[end])
                begin = begin + 1
                end = end - 1

        return LinkedList(input_linked_lists_list[0]).output_list()

    @staticmethod
    def merge_two_sorted_linked_lists(node1, node2):
        """Merge K Sorted Linked Lists Divide and Conquer

        Args:
            node1: First node
            node2: Second node
        Returns:
            Node

        Raises:
            None
        """
        merged_list = LinkedList()

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

        return merged_list.head
