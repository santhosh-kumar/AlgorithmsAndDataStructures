"""
Unit Test for hash_table
"""
from unittest import TestCase

from common.hash_table import HashTable


class TestHashTable(TestCase):
    """
    Unit test for HashTable
    """

    def test_construct(self):
        """Test for construct

        Args:
            self: TestHashTable

        Returns:
            None

        Raises:
            None
        """
        # Given
        hash_table = HashTable()
        hash_table.set("language", "python")
        hash_table.set("language", "c++")
        hash_table.set("language", "java")
        hash_table.set("language", "golang")
        hash_table.set("language", "javascript")
        hash_table.set("os", "android")
        hash_table.set("os", "ios")
        hash_table.set("os", "windows")
        hash_table.set("os", "macosx")

        # Then
        self.assertIsNotNone(hash_table.get("language"))
        self.assertIsNotNone(hash_table.get("os"))
        self.assertTrue(hash_table.has("os"))
        self.assertTrue(hash_table.has("language"))

        # delete
        hash_table.delete("os")
        self.assertFalse(hash_table.has("os"))
