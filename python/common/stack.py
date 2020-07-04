"""
This module defines the stack (FILO) data structure
"""


class Stack:
    """
    An implementation of stack.
    """

    def __init__(self):
        """init stack
        Args:

        Returns:
            None

        Raises:
            None
        """
        self.data_list = []

    def push(self, data):
        """push an element to the stack
        Args:
            data: to be pushed to the stack
        Returns:
            None

        Raises:
            None
        """
        self.data_list.append(data)

    def pop(self):
        """pop the top element from the stack
        Args:

        Returns:
            data

        Raises:
            None
        """
        if len(self) > 0:
            return self.data_list.pop()
        else:
            return None

    def peek(self):
        """peek the top element of the stack
        Args:

        Returns:
            data

        Raises:
            None
        """
        if len(self) > 0:
            return self.data_list[-1]
        else:
            return None

    def __len__(self):
        """len of the stack
        Args:

        Returns:
            size of the stack - int

        Raises:
            None
        """
        return len(self.data_list)
