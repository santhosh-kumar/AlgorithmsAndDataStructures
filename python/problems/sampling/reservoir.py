"""
Reservoir Sampling

Reservoir sampling is a family of randomized algorithms for randomly choosing k samples from a list of n items,
where n is either a very large or unknown number.

Typically n is large enough that the list doesn’t fit into main memory. For example, a list of search queries in Google and Facebook.

So we are given a big array (or stream) of numbers (to simplify),
and we need to write an efficient function to randomly select k numbers where 1 <= k <= n.
"""
import random

from common.problem import Problem


class ReservoirSampling(Problem):
    """
    Reservoir Sampling
    """
    PROBLEM_NAME = "ReservoirSampling"

    def __init__(self, input_list, number_samples):
        """Reservoir Sampling

        Args:
            input_list: Contains a list of integers
            number_samples: Number of elements to sample

        Returns:
            None

        Raises:
            None
        """
        assert (len(input_list) > 0)
        assert (number_samples <= len(input_list))

        super().__init__(self.PROBLEM_NAME)
        self.input_list = input_list
        self.number_samples = number_samples

    def solve(self):
        """Solve the problem

        Note: O(n) (runtime) solution works by copying "k" elements to the reservoir from the stream.
        Then, from i = k+1 to n, a random index is generated, if it's lesser than k, the randomly generated
        index in reservoir is replaced with the ith index.

        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        i = 0

        reservoir = [0] * self.number_samples

        # Initialize it with first k elements from input_list[]
        for i in range(self.number_samples):
            reservoir[i] = self.input_list[i]

        while i < len(self.input_list):
            j = random.randrange(i + 1)

            if j < self.number_samples:
                reservoir[j] = self.input_list[i]

            i = i + 1

        return reservoir
