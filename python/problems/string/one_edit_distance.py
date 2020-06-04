"""
One Edit Distance

Given two strings S and T, determine if they are both one edit distance apart.

Hint:
1. If | n – m | is greater than 1, we know immediately both are not one-edit distance
apart.

2. It might help if you consider these cases separately, m == n and m ≠ n.

3. Assume that m is always ≤ n, which greatly simplifies the conditional statements.
If m > n, we could just simply swap S and T.

4. If m == n, it becomes finding if there is exactly one modified operation. If m ≠ n,
you do not have to consider the delete operation. Just consider the insert operation
in T.
"""
from common.problem import Problem


class OneEditDistance(Problem):
    """
    OneEditDistance
    """
    PROBLEM_NAME = "OneEditDistance"

    def __init__(self, input_string1, input_string2):
        """One Edit Distance

        Args:
            input_string1: string 1 to be compared
            input_string2: string 2 to be compared
        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_string1 = input_string1
        self.input_string2 = input_string2

    def solve(self):
        """Solve the problem
        Note: O(n) (runtime) and O(1) (space) solutions works by iterating over both the strings at the same while updating the edit counter.
        It's important to consider Modify, Append and Insertion operations.

        Args:

        Returns:
            boolean

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        length1 = len(self.input_string1)
        length2 = len(self.input_string2)

        # Check length conditions
        if length1 == 0 and length2 == 0:
            return True

        if abs(length1 - length2) > 2:
            return False

        # adjust to have shorter string at 1
        if length1 > length2:
            tmp = self.input_string2
            self.input_string2 = self.input_string1
            self.input_string1 = tmp

        edit_counter = 0
        j = 0
        i = 0
        while i < length2:
            char1 = None
            if j < length1:
                char1 = self.input_string1[j]

            char2 = None
            if i < length2:
                char2 = self.input_string2[i]

            if char1 is not None and char2 is not None:
                if not char1 == char2:
                    edit_counter = edit_counter + 1
                    if abs(length2 - length1) > 0:
                        # skip incrementing j for insertion operation
                        i = i + 1
            elif char1 is None or char2 is None:
                # this is an append operation
                edit_counter = edit_counter + 1

            # update indexes
            i = i + 1
            j = j + 1

        if edit_counter > 1:
            return False

        return True
