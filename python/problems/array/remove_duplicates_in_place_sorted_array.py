"""
Remove Duplicates In-Place For a Sorted Array

Given a sorted array, the task is to remove the duplicate elements from the array.

Examples:

Input  : arr[] = {2, 2, 2, 2, 2}
Output : arr[] = {2}
         new size = 1

Input  : arr[] = {1, 2, 2, 3, 4, 4, 4, 5, 5}
Output : arr[] = {1, 2, 3, 4, 5}
         new size = 5
"""
from common.problem import Problem


class RemoveDuplicatesInPlaceSortedArray(Problem):
    """
    RemoveDuplicatesInPlaceSortedArray
    """
    PROBLEM_NAME = "RemoveDuplicatesInPlaceSortedArray"

    def __init__(self, input_list):
        """RemoveDuplicatesInPlaceSortedArray

        Args:
            input_list: Contains a list of integers

        Returns:
            None

        Raises:
            None
        """
        assert (len(input_list) > 0)

        super().__init__(self.PROBLEM_NAME)
        self.input_list = input_list

    def solve(self):
        """Solve the problem

        Note: The O(n) runtime and O(1) (space).

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        i = 0
        while i < len(self.input_list):
            j = i + 1

            # iterate till we find the next non-duplicate and an increasing value
            while j < len(self.input_list) and (
                    self.input_list[i] == self.input_list[j] or self.input_list[i] > self.input_list[j]):
                j = j + 1

            # swap with the next position if within the allowed size
            if (i + 1) < len(self.input_list) and j < len(self.input_list):
                self.input_list[i + 1], self.input_list[j] = self.input_list[j], self.input_list[i + 1]
            else:
                # we have reached the end w.r.t. j and hence return now
                return i

            i = i + 1

        return i
