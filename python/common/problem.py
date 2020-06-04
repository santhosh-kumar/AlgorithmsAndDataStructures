"""
This module defines problem abstraction
"""
from abc import ABCMeta, abstractmethod


class Problem:
    """
    Abstraction for Analysis
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, problem_name):
        """Init

        Args:
            problem_name: name of the problem

        Returns:
            None

        Raises:
            None
        """
        self.problem_name = problem_name

    @abstractmethod
    def solve(self):
        """Runs the solve for the problem

        Args:

        Raises:
            None
        """
        raise NotImplementedError
