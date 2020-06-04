"""
Climbing Stairs

You are climbing a staircase. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to
the top?
"""
from common.problem import Problem


class ClimbingStairs(Problem):
    """
    ClimbingStairs
    """
    PROBLEM_NAME = "ClimbingStairs"

    def __init__(self, number_steps):
        """Climbing Stairs

        Args:
            number_steps: number of steps

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.number_steps = number_steps

    def solve(self):
        """Solve the problem

        Note: O(n) (runtime) solution uses dynamic programming to calculate the number of ways
        by adding number of ways to reach one step before with number of ways to reach two steps before the current step.

        Alternatively, the recursive solution can use the same method as solving the Fibonacci series.
        Nth integer in the Fibonacci series is the number of ways.

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        if self.number_steps <= 2:
            return self.number_steps

        one_step_before = 2
        two_steps_before = 1

        number_ways = 0

        for i in range(2, self.number_steps):
            number_ways = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = number_ways

        return number_ways
