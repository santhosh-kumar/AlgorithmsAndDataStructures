"""
Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not,
return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""
from common.problem import Problem


class SearchInsertPosition(Problem):
    """
    SearchInsertPosition
    """
    PROBLEM_NAME = "SearchInsertPosition"

    def __init__(self, input_list, element_to_insert):
        """Search Insert Position

        Args:
            input_list: Contains a list of integers
            element_to_insert: Element to insert
        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_list = input_list
        self.element_to_insert = element_to_insert

    def solve(self):
        """Solve the problem

        Note: O(log n) (runtime) splits the array in the middle and checks if the item belongs to the right or the left side.

        Args:

        Returns:
            string

        Raises:
            None
        """
        left = 0
        right = len(self.input_list) - 1

        while left < right:
            middle = int((left + right) / 2)

            if self.input_list[middle] < self.element_to_insert:
                left = middle + 1
            else:
                right = middle

        if self.input_list[left] < self.element_to_insert:
            return left + 1
        else:
            return left
