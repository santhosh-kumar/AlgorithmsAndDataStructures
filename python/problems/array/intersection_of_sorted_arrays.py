"""
Intersection Of Sorted Arrays

Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example :

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 5]

Output : [3 5]
"""
from common.problem import Problem


class IntersectionOfSortedArrays(Problem):
    """
    Two Sum
    """
    PROBLEM_NAME = "IntersectionOfSortedArrays"

    def __init__(self, input_list1, input_list2):
        """Intersection of sorted arrays

        Args:
            input_list1: First array
            input_list2: Second array

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_list1 = input_list1
        self.input_list2 = input_list2

    def solve(self):
        """Solve the problem

        Note: O(m+n) (runtime)

        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        len1 = len(self.input_list1)
        len2 = len(self.input_list2)

        i = 0
        j = 0

        result = []
        while i < len1 and j < len2:
            if self.input_list1[i] < self.input_list2[j]:
                i = i + 1
            elif self.input_list2[j] < self.input_list1[i]:
                j = j + 1
            else:
                result.append(self.input_list1[i])
                i = i + 1
                j = j + 1

        return result
