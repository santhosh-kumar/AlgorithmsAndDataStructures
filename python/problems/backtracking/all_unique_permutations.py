"""
All Unique Permutations

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example :
[1,1,2] have the following unique permutations:

[1,1,2]
[1,2,1]
[2,1,1]
"""
from common.problem import Problem


class AllUniquePermutations(Problem):
    """
    AllUniquePermutations
    """
    PROBLEM_NAME = "AllUniquePermutations"

    def __init__(self, input_list):
        """AllUniquePermutations

        Args:
            input_list: Contains a list of integers

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_list = input_list

    def solve(self):
        """Solve the problem

        Note: O(|V|+|E|) (runtime) because it's a tree structure.
              Reference: https://medium.com/algorithms-and-leetcode/backtracking-e001561b9f28

        Args:

        Returns:
            list(list)

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        result = []
        used = [False] * len(self.input_list)
        current = []
        depth = 0

        self.permute(depth, used, current, result)

        return result

    def permute(self, depth, used, current, result):
        """permute the list

        Args:
            depth: start from 0, and represent the depth of the search
            used: track what items are  in the partial solution from the set of n
            current: the current partial solution
            result: collect all the valid solutions

        Returns:

        Raises:
            None
        """
        if depth == len(self.input_list):
            # use deepcopy because curr is tracking all partial solution, it eventually become []
            result.append(current[::])
            return

        for i in range(len(self.input_list)):
            if not used[i]:
                current.append(self.input_list[i])
                used[i] = True

                # move to the next depth
                self.permute(depth + 1, used, current, result)

                # backtrack to previous partial state
                current.pop()
                used[i] = False

        return
