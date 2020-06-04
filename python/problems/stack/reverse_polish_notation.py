"""
Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
 ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
 ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

Example Questions Candidate Might Ask:
Q: Is an empty array a valid input?
A: No.
"""
from common.problem import Problem
from common.stack import Stack


class ReversePolishNotation(Problem):
    """
    ReversePolishNotation
    """
    PROBLEM_NAME = "ReversePolishNotation"
    OPERATORS = ["+", "-", "*", "/"]

    def __init__(self, input_list):
        """Reverse Polish Notation

        Args:
            input_string: input_string evaluated using reverse polish notation
        Returns:
            None

        Raises:
            None
        """
        assert (len(input_list) > 0)

        super().__init__(self.PROBLEM_NAME)
        self.input_list = input_list

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

        notation_stack = Stack()
        for i in range(len(self.input_list)):
            if self.input_list[i] not in self.OPERATORS:
                notation_stack.push(self.input_list[i])
            else:
                operand2 = int(notation_stack.pop())
                assert operand2 is not None, "Invalid operand2"

                operand1 = int(notation_stack.pop())
                assert operand1 is not None, "Invalid operand1"

                result = self.evaluate(operand1, operand2, self.input_list[i])

                notation_stack.push(result)

        return notation_stack.pop()

    @staticmethod
    def evaluate(operand1, operand2, operator):
        """Evaluates the operation using the operator and operands
        Args:
            operand1: first argument
            operand2: second argument
            operator: operator

        Returns:
            integer

        Raises:
            None
        """
        if operator == "+":
            return operand1 + operand2
        elif operator == "-":
            return operand1 - operand2
        elif operator == "*":
            return operand1 * operand2
        else:
            return operand1 / operand2
