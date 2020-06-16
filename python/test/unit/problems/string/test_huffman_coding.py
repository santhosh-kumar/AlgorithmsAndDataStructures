"""
Unit Test for huffman_coding
"""
from unittest import TestCase

from problems.string.huffman_coding import HuffmanCoding


class TestHuffmanCoding(TestCase):
    """
    Unit test for HuffmanCoding
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestHuffmanCoding

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "thisisatestmessageforencoding"
        huffman_coding_problem = HuffmanCoding(input_string)

        # When
        result = huffman_coding_problem.solve()

        # Then
        self.assertEqual(result,
                         "010101011111001111000110010100000101100010000000110101110010100111011001100110101110111001111111111011011")
