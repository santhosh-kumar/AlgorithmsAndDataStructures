"""
Pretty Print JSON

Given a string A representating json object. Return an array of string denoting json object with proper indentaion.

Rules for proper indentaion:

Every inner brace should increase one indentation to the following lines.
Every close brace should decrease one indentation to the same line and the following lines.
The indents can be increased with an additional ‘\t’
Note:

[] and {} are only acceptable braces in this case.

Assume for this problem that space characters can be done away with.

For Example

Input 1:
    A = "{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}"

Output 1:
    {
        A:"B",
        C:
        {
            D:"E",
            F:
            {
                G:"H",
                I:"J"
            }
        }
    }

Input 2:
    A = ["foo", {"bar":["baz",null,1.0,2]}]
Output 2:
   [
        "foo",
        {
            "bar":
            [
                "baz",
                null,
                1.0,
                2
            ]
        }
    ]
"""
import os

from common.problem import Problem


class PrettyPrintJSON(Problem):
    """
    PrettyPrintJSON
    """
    PROBLEM_NAME = "PrettyPrintJSON"

    OPENING_BRACKETS = ['{', '[']
    CLOSING_BRACKETS = ['}', ']']
    COMMA = ','
    SPACE = ' '

    def __init__(self, input_string):
        """Pretty Print JSON

        Note:

        Args:
            input_string: JSON string to be pretty-printed

        Returns:
            None

        Raises:
            None
        """
        assert (len(input_string) > 0)

        super().__init__(self.PROBLEM_NAME)
        self.input_string = input_string

    def solve(self):
        """Solve the problem
        Args:

        Returns:
            string

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        json = self.input_string

        if not json:
            return ''

        result = []
        multiplier = 0
        i = 0

        while i < len(json):
            if json[i] in self.OPENING_BRACKETS:
                result.append(self.SPACE * multiplier + json[i])
                multiplier = multiplier + 1
                i = i + 1

            elif json[i] in self.CLOSING_BRACKETS:
                multiplier = multiplier - 1
                result.append(self.SPACE * multiplier + json[i])
                i = i + 1

            elif json[i] == self.COMMA:
                result[-1] = result[-1] + self.COMMA
                i = i + 1

            else:
                start = i
                while i < len(json) and json[i] not in self.OPENING_BRACKETS + [self.COMMA] + self.CLOSING_BRACKETS:
                    i = i + 1

                temp = json[start:i]
                result.append(self.SPACE * multiplier + temp)

        result_string = ""
        for st in result:
            result_string = result_string + st + os.linesep

        return result_string
