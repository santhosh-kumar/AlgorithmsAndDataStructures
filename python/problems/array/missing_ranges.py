"""
Missing Ranges

Given a sorted integer array where the range of elements are [0, 99] inclusive, return its missing ranges.

For example, given [0, 1, 3, 50, 75], return [“2”, “4->49”, “51->74”, “76->99”]

Example Questions Candidate Might Ask:

Q: What if the given array is empty?
A: Then you should return [“0->99”] as those ranges are missing.

Q: What if the given array contains all elements from the ranges?
A: Return an empty list, which means no range is missing.
"""
from common.problem import Problem


class MissingRanges(Problem):
    """
    MissingRanges
    """
    PROBLEM_NAME = "MissingRanges"

    def __init__(self, input_list, min_value, max_value):
        """Missing Ranges

        Args:
            input_list: Contains a list of integers
        Returns:
            None

        Raises:
            None
        """
        # assert (min_value <= max_value, "Invalid min or max values")
        super().__init__(self.PROBLEM_NAME)
        self.input_list = input_list
        self.min_value = min_value
        self.max_value = max_value

    def solve(self):
        """Solve the problem
        Note: O(n) (runtime) and O(1) (space) works by iterating the input_list and checking boundary conditions w.r.t. min_value and max_value.

        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        if len(self.input_list) == 0:
            return range(0, self.max_value + 1)

        range_list = []

        for i in range(len(self.input_list)):
            if i == 0 and self.input_list[i] == self.min_value:
                continue
            elif i == 0 and (self.input_list[i] - self.min_value) > 2:
                missing_range = "{}->{}".format(self.min_value, self.input_list[i] - 1)
                range_list.append(missing_range)
                continue
            elif i == 0 and (self.input_list[i] - self.min_value) == 1:
                missing_range = self.min_value
                range_list.append(str(missing_range))
                continue

            if (self.input_list[i] - self.input_list[i - 1]) > 2:
                missing_range = "{}->{}".format(self.input_list[i - 1] + 1, self.input_list[i] - 1)
                range_list.append(missing_range)
            elif (self.input_list[i] - self.input_list[i - 1]) == 2:
                missing_range = self.input_list[i] - self.input_list[i - 1]
                range_list.append(str(missing_range))

            if i == len(self.input_list) - 1 and (self.max_value - self.input_list[i]) > 2:
                missing_range = "{}->{}".format(self.input_list[i] + 1, self.max_value)
                range_list.append(missing_range)
                continue
            elif i == len(self.input_list) - 1 and (self.max_value - self.input_list[i]) == 2:
                missing_range = self.max_value
                range_list.append(str(missing_range))
                continue

        return range_list
