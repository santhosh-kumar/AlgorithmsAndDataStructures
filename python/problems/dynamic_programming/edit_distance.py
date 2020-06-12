"""
Edit Distance

Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.

Insert
Remove
Replace

All of the above operations are of equal cost.

Examples:

Input:   str1 = "geek", str2 = "gesek"
Output:  1
We can convert str1 into str2 by inserting a 's'.

Input:   str1 = "cat", str2 = "cut"
Output:  1
We can convert str1 into str2 by replacing 'a' with 'u'.

Input:   str1 = "sunday", str2 = "saturday"
Output:  3
Last three and first characters are same.  We basically
need to convert "un" to "atur".  This can be done using
below three operations.

Replace 'n' with 'r', insert t, insert a
"""
from common.problem import Problem


class EditDistance(Problem):
    """
    EditDistance
    """
    PROBLEM_NAME = "EditDistance"

    def __init__(self, input_string1, input_string2):
        """EditDistance

        Args:
            input_string1: First string
            input_string1: Second string

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

        Note: O(mn) (runtime) and O(mn) (space) solution works by filling up the distance matrix.

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        len1 = len(self.input_string1)
        len2 = len(self.input_string2)

        distance_matrix = [[0 for x in range(len2 + 1)] for x in range(len1 + 1)]

        for i in range(len1 + 1):
            for j in range(len2 + 1):
                # If first string is empty, only option is to
                # insert all characters of second string
                if i == 0:
                    distance_matrix[i][j] = j  # Min. operations = j

                # If second string is empty, only option is to
                # remove all characters of second string
                elif j == 0:
                    distance_matrix[i][j] = i  # Min. operations = i

                # If last characters are same, ignore last char
                # and recur for remaining string
                elif self.input_string1[i - 1] == self.input_string2[j - 1]:
                    distance_matrix[i][j] = distance_matrix[i - 1][j - 1]

                # If last characters are different, consider all
                # possibilities and find minimum
                else:
                    distance_matrix[i][j] = 1 + min(distance_matrix[i][j - 1],  # Insert
                                                    distance_matrix[i - 1][j],  # Remove
                                                    distance_matrix[i - 1][j - 1]  # Update
                                                    )

        return distance_matrix[len1][len2]
