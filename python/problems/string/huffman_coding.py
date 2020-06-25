"""
Huffman Coding

Huffman compression is one of the fundamental lossless compression algorithms.

It banks on the basic idea of representing the most common recurring subunit with the least number of bits.
A lot of the time, this recurring subunit may be a character, like we are assuming in this article.


"""
import heapq
from collections import defaultdict

from common.problem import Problem


class HuffmanCoding(Problem):
    """
    HuffmanCoding
    """
    PROBLEM_NAME = "HuffmanCoding"

    def __init__(self, input_string):
        """Huffman Coding

        Args:
            input_string: input_string to be encoded

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_string = input_string

    def solve(self):
        """Solve the problem

        Note: O(n logn) solution uses heapq for encoding the characters based on frequencies.

        Args:

        Returns:
            None

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        frequency_dict = self.get_characters_frequency(self.input_string)
        huffman_code_dict = self.encode(frequency_dict)

        encoded_string = ""
        for ch in self.input_string:
            encoded_string = encoded_string + huffman_code_dict[ch]

        return encoded_string

    @staticmethod
    def encode(frequency_dict):
        """Encode

        Args:
            frequency_dict: Characters frequency dict

        Returns:
            dict

        Raises:
            None
        """
        heap = [[weight, [symbol, '']] for symbol, weight in frequency_dict.items()]

        heapq.heapify(heap)
        while len(heap) > 1:
            low = heapq.heappop(heap)
            high = heapq.heappop(heap)

            for value in low[1:]:
                value[1] = '0' + value[1]

            for value in high[1:]:
                value[1] = '1' + value[1]

            heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])

        huffman_code_dict = {}
        for value in heapq.heappop(heap)[1:]:
            huffman_code_dict[value[0]] = value[1]

        return huffman_code_dict

    @staticmethod
    def get_characters_frequency(input_string):
        """Get Characters frequency in a given string

        Args:
            input_string: input string

        Returns:
            defaultdict(int)

        Raises:
            None
        """
        frequency_dict = defaultdict(int)
        for ch in input_string:
            frequency_dict[ch] = frequency_dict[ch] + 1

        return frequency_dict
