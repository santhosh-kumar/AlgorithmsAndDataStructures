"""
This module defines the heap data structure
"""
import math
from abc import ABCMeta


class Heap:
    """
    Base class for min/max heap
    """
    __metaclass__ = ABCMeta

    def __init__(self, elements_list):
        """init heap
        Args:
            elements_list: List of elements to initialize heap with

        Returns:
            None

        Raises:
            None
        """
        self.elements_list = []

        # add elements to the heap
        if len(elements_list) > 0:
            self.build_heap(elements_list)

    def __len__(self):
        """Return the size of the heap
        Args:

        Returns:
            integer

        Raises:
            None
        """
        return len(self.elements_list)

    def height(self):
        """Returns the height of the heap
        Args:

        Returns:
            integer

        Raises:
            None
        """
        # example: for 7 nodes, height = ceil(log(7)/log(2)) ~ 3
        return math.ceil((math.log(len(self))) / math.log(2))

    def is_leaf(self, i):
        """Returns true if it's a leaf node
        Args:
            i: index of the node
        Returns:
            boolean

        Raises:
            None
        """
        # example: for 7 nodes, i > ceil(5/2) = 3 are the leaf nodes
        return i > int(math.ceil((len(self) - 2) / 2.0))

    def heap_push(self, element):
        """insert an element
        Args:
            element: to be inserted to the heap

        Returns:
            None

        Raises:
            None
        """
        raise NotImplementedError

    def heap_pop(self):
        """delete the root
        Args:

        Returns:
            object

        Raises:
            None
        """
        if len(self) > 0:
            # swap the root element with the laste element
            self.elements_list[0], self.elements_list[-1] = self.elements_list[-1], self.elements_list[0]

            # pop the last element
            element = self.elements_list.pop()

            #
            self.heapify(0)
            return element
        else:
            return None

    def peek(self):
        """peek the next element without deleting
        Args:

        Returns:
            Object

        Raises:
            None
        """
        if len(self) > 0:
            return self.elements_list[0]
        else:
            return None

    def build_heap(self, elements_list):
        """Build a heap with the given elements list

        Args:
            elements_list: to build heap with

        Returns:
            None

        Raises:
            None
        """
        self.elements_list = elements_list[:]

        # for example, with 7 nodes, parent node would be at the index 3.
        last_leaf_index = self.parent(len(self))

        # iterate from the last leaf index to the root
        for i in range(last_leaf_index, -1, -1):
            self.heapify(i)

    def heapify(self):
        """heapify the array
        Args:

        Returns:
            None

        Raises:
            None
        """
        raise NotImplementedError

    @staticmethod
    def parent(i):
        """Returns the parent index
        Args:
            i: index of the node under consideration

        Returns:
            integer

        Raises:
            None
        """
        if i == 0:
            return -1
        elif i % 2 == 0:
            return int((i - 2) / 2)
        else:
            return int((i - 1) / 2)

    @staticmethod
    def left_child(i):
        """Returns the left_child index
        Args:
            i: index of the node under consideration

        Returns:
            integer

        Raises:
            None
        """
        return i * 2 + 1

    @staticmethod
    def right_child(i):
        """Returns the right_child index
        Args:
            i: index of the node under consideration

        Returns:
            integer

        Raises:
            None
        """
        return i * 2 + 2


class MinHeap(Heap):
    """
    Implements min heap (<)
    """

    def __init__(self, elements_list):
        """init heap
        Args:
            elements_list: List of elements to initialize heap with

        Returns:
            None

        Raises:
            None
        """
        super().__init__(elements_list)

    def heapify(self, i):
        """heapify the array
        Args:
            i: index of the current element

        Returns:
            None

        Raises:
            None
        """
        # get the right and left children indices
        left_child_index = self.left_child(i)
        right_child_index = self.right_child(i)

        # set the current index as the smallest
        smallest_index = i

        # update smallest index to the left child index if it's greater than the left child
        if left_child_index < len(self) and self.elements_list[left_child_index] < self.elements_list[smallest_index]:
            smallest_index = left_child_index

        # update smallest index to the right child index if it's greater than the right child
        if right_child_index < len(self) and self.elements_list[right_child_index] < self.elements_list[smallest_index]:
            smallest_index = right_child_index

        # swap current element with the smallest
        if smallest_index != i:
            self.elements_list[i], self.elements_list[smallest_index] = self.elements_list[smallest_index], \
                                                                        self.elements_list[i]

            # recursively call the heapify from the current smallest_index
            self.heapify(smallest_index)

    def heap_push(self, element):
        """insert an element
        Args:
            element: to be inserted to the heap

        Returns:
            None

        Raises:
            None
        """
        i = len(self)

        # append the element to the end of the list
        self.elements_list.append(element)

        # get the parent index
        parent_index = self.parent(i)

        # while the element is lesser than the parent, keep swapping and update the index of the current node to parent
        # this done till we reach the root node
        while parent_index != -1 and self.elements_list[i] < self.elements_list[parent_index]:
            self.elements_list[i], self.elements_list[parent_index] = self.elements_list[parent_index], \
                                                                      self.elements_list[i]
            i = parent_index
            parent_index = self.parent(i)


class MaxHeap(Heap):
    """
    Implements max heap (>)
    """

    def __init__(self, elements_list):
        """init heap
        Args:
            elements_list: List of elements to initialize heap with

        Returns:
            None

        Raises:
            None
        """
        super().__init__(elements_list)

    def heapify(self, i):
        """heapify the array
        Args:
            i: index of the current element

        Returns:
            None

        Raises:
            None
        """
        # get the right and left children indices
        left_child_index = self.left_child(i)
        right_child_index = self.right_child(i)

        # set the current index as the smallest
        smallest_index = i

        # update smallest index to the left child index if it's greater than the left child
        if left_child_index < len(self) and self.elements_list[left_child_index] > self.elements_list[smallest_index]:
            smallest_index = left_child_index

        # update smallest index to the right child index if it's greater than the right child
        if right_child_index < len(self) and self.elements_list[right_child_index] > self.elements_list[smallest_index]:
            smallest_index = right_child_index

        # swap current element with the smallest
        if smallest_index != i:
            self.elements_list[i], self.elements_list[smallest_index] = self.elements_list[smallest_index], \
                                                                        self.elements_list[i]

            # recursively call the heapify from the current smallest_index
            self.heapify(smallest_index)

    def heap_push(self, element):
        """insert an element
        Args:
            element: to be inserted to the heap

        Returns:
            None

        Raises:
            None
        """
        i = len(self)

        # append the element to the end of the list
        self.elements_list.append(element)

        # get the parent index
        parent_index = self.parent(i)

        # while the element is lesser than the parent, keep swapping and update the index of the current node to parent
        # this done till we reach the root node
        while parent_index != -1 and self.elements_list[i] > self.elements_list[parent_index]:
            self.elements_list[i], self.elements_list[parent_index] = self.elements_list[parent_index], \
                                                                      self.elements_list[i]
            i = parent_index
            parent_index = self.parent(i)
