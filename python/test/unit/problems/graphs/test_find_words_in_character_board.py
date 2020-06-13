"""
Unit Test for all_pairs_shortest_path_floyd_warshall
"""
from unittest import TestCase

from problems.graphs.find_words_in_a_character_board import FindWordsInABoardOfCharacters


class TestFindWordsInABoardOfCharacters(TestCase):
    """
    Unit test for FindWordsInABoardOfCharacters
    """

    def test_solve(self):
        """Test solve

        Args:
            self: FindWordsInABoardOfCharacters

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_characters_matrix = [['G', 'I', 'Z'], ['U', 'E', 'K'], ['Q', 'S', 'E']]
        dictionary = {"GEEKS", "FOR", "QUIZ", "GO"}
        find_words_problem = FindWordsInABoardOfCharacters(input_characters_matrix, dictionary)

        # When
        result = find_words_problem.solve()

        # Then
        self.assertEqual(result, ['GEEKS', 'QUIZ'])
