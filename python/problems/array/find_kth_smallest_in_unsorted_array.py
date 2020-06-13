"""
Find Kth smallest in a unsorted array

Given an array and a number k where k is smaller than size of array,
we need to find the k’th smallest element in the given array.
It is given that ll array elements are distinct.
"""
import heapq

from common.problem import Problem


class FindKthSmallestInUnsortedArray(Problem):
    """
    Find Kth smallest in a unsorted array
    """
    PROBLEM_NAME = "FindKthSmallestInUnsortedArray"

    def __init__(self, input_list, K):
        """Find Kth smallest in a unsorted array

        Args:
            input_list: Contains a list of integers
            K: th element to return

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_list = input_list
        self.K = K

    def solve(self):
        """Solve the problem

        Note: O(N + KLogN) (runtime) complexity using the min-heap.

        Args:

        Returns:
            tuple

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        input_list = self.input_list

        heapq.heapify(input_list)

        k = 1
        while True:
            element = heapq.heappop(input_list)
            if k == self.K:
                return element
            k = k + 1
