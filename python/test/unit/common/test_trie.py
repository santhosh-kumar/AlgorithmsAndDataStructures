"""
Unit Test for trie
"""
from unittest import TestCase

from common.trie import Trie


class TestTrie(TestCase):
    """
    Unit test for Trie
    """

    def test_find_prefix(self):
        """Test for find_prefid

        Args:
            self: TestTrie

        Returns:
            None

        Raises:
            None
        """
        # Given
        trie_obj = Trie()

        # When
        trie_obj.add("hello")
        trie_obj.add("hell")
        trie_obj.add("he")
        trie_obj.add("she")

        # Then
        self.assertEqual(trie_obj.find_prefix("he"), (True, 3))
        self.assertEqual(trie_obj.find_prefix("hell"), (True, 2))
        self.assertEqual(trie_obj.find_prefix("hello"), (True, 1))
        self.assertEqual(trie_obj.find_prefix("h"), (True, 3))
        self.assertEqual(trie_obj.find_prefix("me"), (False, 0))
