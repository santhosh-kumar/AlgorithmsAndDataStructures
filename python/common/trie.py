"""
This module defines the trie data structure
"""


class TrieNode:
    """
    An abstraction of a trie node.
    """

    def __init__(self, character):
        """init
        Args:
            character: to be inserted

        Returns:
            None

        Raises:
            None
        """
        self.character = character
        self.children = []
        self.is_word_end = False
        self.counter = 1

    def add_child(self, node):
        """Add a child node
        Args:
            node: child node

        Returns:
            None

        Raises:
            None
        """
        self.children.append(node)

    def get_children_count(self):
        """Get the number of children
        Args:

        Returns:
            integer

        Raises:
            None
        """
        return len(self.children)


class Trie:
    """
    An implementation of a trie data structure.
    """

    def __init__(self):
        """init
        Args:

        Returns:
            None

        Raises:
            None
        """
        self.root = TrieNode('*')

    def add(self, word):
        """Add a word to the trie
        Args:
            word: to be added to the trie

        Returns:
            None

        Raises:
            None
        """
        node = self.root

        for character in word:
            is_found = False

            for child in node.children:
                if child.character == character:
                    is_found = True
                    child.counter = child.counter + 1
                    node = child
                    break

            if not is_found:
                new_node = TrieNode(character)
                node.add_child(new_node)
                node = new_node

        node.is_word_end = True

    def find_prefix(self, prefix):
        """Search for a word in the trie
        Args:
            prefix: to be found

        Returns:
            tuple -- (word prefix present, how many words)

        Raises:
            None
        """
        node = self.root

        if node.get_children_count() <= 0:
            return False, 0

        for character in prefix:
            is_found = False

            for child in node.children:
                if character == child.character:
                    is_found = True
                    node = child
                    break

            if not is_found:
                return False, 0

        return True, node.counter
