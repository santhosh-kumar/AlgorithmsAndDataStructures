"""
Merge K Sorted Linked Lists Priority Queue (Heap based solution)

Merge k sorted linked lists and return it as a new list. The new list should be made by
splicing together the nodes of the first two list.
"""
import heapq

from common.problem import Problem


class MergeKSortedLinkedListsPriorityQueue(Problem):
    """
    Merge K Sorted Linked Lists Priority Queue
    """
    PROBLEM_NAME = "MergeKSortedLinkedListsPriorityQueue"

    def __init__(self, input_linked_lists_list):
        """Merge K Sorted Linked Lists Priority Queue

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

        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        priority_queue = []

        # Add the head node (smallest) to the heap
        for k in range(len(self.input_linked_lists_list)):
            heapq.heappush(priority_queue,
                           (self.input_linked_lists_list[k].head.data, self.input_linked_lists_list[k].head))

        merged_list = []

        if len(priority_queue) == 0:
            return merged_list

        data, node = heapq.heappop(priority_queue)
        while node is not None:
            merged_list.append(node.data)

            if node.next_node is not None:
                heapq.heappush(priority_queue, (node.next_node.data, node.next_node))

            if len(priority_queue) > 0:
                data, node = heapq.heappop(priority_queue)
            else:
                node = None

        return merged_list
