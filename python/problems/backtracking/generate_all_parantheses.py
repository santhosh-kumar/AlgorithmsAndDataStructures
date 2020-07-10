"""
Generate Parantheses

Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The combinations themselves must be sorted in ascending order.
CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR … (a1 = b1 AND a2 = b2 AND … ai = bi AND ai+1 > bi+1)
The solution set must not contain duplicate combinations.

Example,
Given candidate set 2,3,6,7 and target 7,
A solution set is:

[2, 2, 3]
[7]
"""
from common.problem import Problem


class CombinationSum(Problem):
    """
    CombinationSum
    """
    PROBLEM_NAME = "CombinationSum"

    def __init__(self, input_list, target_sum):
        """CombinationSum

        Args:
            input_list: Contains a list of integers
            target_sum: Target sum to add upto

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_list = input_list
        self.target_sum = target_sum

    def solve(self):
        """Solve the problem

        Note:

        Args:

        Returns:
            list(list)

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        # remove duplicates
        self.input_list = list(set(self.input_list))

        # sort the array
        self.input_list.sort()

        result = []
        index = 0
        current = []
        self.find_numbers(result, current, self.target_sum, index)

        return result

    def find_numbers(self, result, current, current_sum, index):
        """Find numbers that add up to the target sum

        Args:
            result: collect all the valid solutions
            current: the current partial solution
            current_sum: Currently computed sum
            index: to start iterating

        Returns:

        Raises:
            None
        """
        # If  current sum becomes negative
        if current_sum < 0:
            return

        # If we get exact answer
        if current_sum == 0:
            result.append(current[::])
            return

        # Recur for all remaining elements that have value smaller than sum.
        while index < len(self.input_list) and current_sum - self.input_list[index] >= 0:
            # Till every element in the array starting from index which can contribute to the sum
            current.append(self.input_list[index])

            # recur for next numbers
            self.find_numbers(result, current, current_sum - self.input_list[index], index)

            index = index + 1

            # remove number from list (backtracking)
            current.pop()

        return
