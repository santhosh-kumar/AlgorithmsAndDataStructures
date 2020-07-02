"""
Unit Test for bloom_filter
"""
from unittest import TestCase

from common.bloom_filter import BloomFilter


class TestBloomFilter(TestCase):
    """
    Unit test for BloomFilter
    """

    def test_bloom_filter(self):
        """Test for construct

        Args:
            self: TestBloomFilter

        Returns:
            None

        Raises:
            None
        """
        # Given
        items_count = 20
        false_positive_probability = 0.05

        bloom_filter = BloomFilter(items_count, false_positive_probability)

        # words to be added
        words_present = ['apple', 'ball', 'cat', 'dog', 'elephant',
                         'fan', 'giraffe', 'hat', 'ink', 'jug', 'kite',
                         'man', 'nurse', 'owl', 'pig', 'queen',
                         'rat', 'star', 'tent', 'umbrella', 'van']

        for item in words_present:
            bloom_filter.add(item)

        # Then
        for item in words_present:
            self.assertTrue(bloom_filter.check(item))

        # these words are not present
        self.assertFalse(bloom_filter.check("test"))
        self.assertFalse(bloom_filter.check("nobody"))
