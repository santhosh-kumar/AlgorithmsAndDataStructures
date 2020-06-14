"""
Count Number of Bits to Flip

Given two numbers ‘a’ and b’. Write a program to count number of bits needed to be flipped to convert ‘a’ to ‘b’.
Example :

Input : a = 10, b = 20
Output : 4
Binary representation of a is 00001010
Binary representation of b is 00010100

We need to flip four bits in a to make it b.
"""

from common.problem import Problem


class CountNumberOfBitsToFlip(Problem):
    """
    CountNumberOfBitsToFlip
    """
    PROBLEM_NAME = "CountNumberOfBitsToFlip"

    def __init__(self, input_number1, input_number2):
        """Count Number of Bits to Flip

        Args:
            input_number1: First number
            input_number2: Second number
        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_number1 = input_number1
        self.input_number2 = input_number2

    def solve(self):
        """Solve the problem

        Note:

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        return self.count_set_bits_with_brian_kernighan_algorithm(self.input_number1 ^ self.input_number2)

    @staticmethod
    def count_set_bits_with_brian_kernighan_algorithm(number):
        """Brian Kernighan's algorithm to count set bits

        Note:
            1  Initialize count: = 0

            2  If integer n is not zero
                (a) Do bitwise & with (n-1) and assign the value back to n
                n: = n&(n-1)
                (b) Increment count by 1
                (c) go to step 2

            3  Else return count

        Args:

        Returns:
            integer

        Raises:
            None
        """
        if number == 0:
            return 0

        return 1 + CountNumberOfBitsToFlip.count_set_bits_with_brian_kernighan_algorithm(number & (number - 1))
