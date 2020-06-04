"""
Two Sum Data Structure

Design and implement a TwoSum class. It should support the following operations: add and find.
add(input) – Add the number input to an internal data structure.
find(value) – Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5); find(4)  true; find(7)  false
"""
from common.problem import Problem


class TwoSumDataStructure(Problem):
    """
    TwoSumDataStructure
    """
    PROBLEM_NAME = "TwoSumDataStructure"

    def __init__(self):
        """Two Sum Data Structure

        Args:

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_dict = {}

    def solve(self):
        """Solve the problem
        Args:

        Returns:
            None

        Raises:
            None
        """
        pass

    def add(self, value):
        """Add a value to the input_dict
        Args:
            value: integer value to be added

        Returns:
            None

        Raises:
            None
        """
        # Note: Adding element to the dict is O(1) operation
        if value in self.input_dict:
            self.input_dict[value] = self.input_dict[value] + 1
        else:
            self.input_dict[value] = 1

    def find(self, target_sum):
        """Find the target sum from the input dict
        Args:
            target_sum: to be found from the input_dict

        Returns:
            Boolean (True|False)

        Raises:
            None
        """

        for key in self.input_dict:
            value_to_find = target_sum - key

            if value_to_find == key:
                # if the value to find is same as the key, it should occur at least twice.
                if self.input_dict[key] >= 2:
                    return True
            if value_to_find in self.input_dict:
                return True

        return False
