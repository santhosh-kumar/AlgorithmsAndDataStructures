"""
Find all possible words in a board of characters (Boggle)

Given a dictionary, a method to do lookup in dictionary and a M x N board where every cell has one character.
Find all possible words that can be formed by a sequence of adjacent characters.

Note that we can move to any of 8 adjacent characters, but a word should not have multiple instances of same cell.
"""
from common.graph import UndirectedGraph
from common.problem import Problem


class FindWordsInABoardOfCharacters(Problem):
    """
    FindWordsInABoardOfCharacters
    """
    PROBLEM_NAME = "FindWordsInABoardOfCharacters"

    def __init__(self, input_characters_matrix, dictionary):
        """Find all possible words in a board of characters (Boggle)

        Args:
            input_characters_matrix: Characters matrix
            dictionary: dictionary of words

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_characters_matrix = input_characters_matrix
        self.dictionary = dictionary

    def solve(self):
        """Solve the problem

        Note: O(n^2) (runtime) complexity uses the DFS for finding words in a boggle board.

        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        graph = self.create_graph()

        characters_list = self.get_characters_list()
        vertices = graph.get_vertices()

        visited = [False] * len(vertices)
        result = []
        current_string = ""

        for vertex in vertices:
            self.find_words(graph, characters_list, vertex, current_string, visited, result)

        return result

    def find_words(self, graph, characters_list, vertex, current_string, visited, result):
        """Find words recursively using the neighbors of the current vertex

        Args:
            graph: Boggle board represented as a graph
            characters_list: List of characters on the board
            vertex: Current vertex
            current_string: Currently processed string
            visited: A list for bookkeeping visited vertices
            result: List of words to return

        Returns:
            None

        Raises:
            None
        """
        # Mark current cell as visited and append current character to the current_string
        visited[vertex] = True
        current_string = current_string + characters_list[vertex]

        # If the word is in the dictionary, add it to the result
        if current_string in self.dictionary:
            result.append(current_string)

        # recursively process the neighbor nodes
        neighbors = graph.get_neighbors(vertex)
        for neighbor_vertex in neighbors:
            if not visited[neighbor_vertex]:
                self.find_words(graph, characters_list, neighbor_vertex, current_string, visited, result)

        # Erase the last appended character and mark the vertex as not visited. Since the same vertex can be in the path of
        # other vertices
        current_string = current_string[:-1]
        visited[vertex] = False

    def create_graph(self):
        """Create a undirected graph

        Args:

        Returns:
            Graph

        Raises:
            None
        """
        graph = UndirectedGraph()
        for i in range(len(self.input_characters_matrix)):
            for j in range(len(self.input_characters_matrix[0])):
                self.add_neighbors(self.input_characters_matrix, i, j, graph)
        return graph

    @staticmethod
    def add_neighbors(input_characters_matrix, i, j, graph):
        """Add neighbors to the graph

        Args:
            input_characters_matrix: Matrix of input characters
            i: row index
            j: column index
            graph: to add the neighbors for

        Returns:
            Graph

        Raises:
            None
        """
        max_rows = len(input_characters_matrix)
        max_columns = len(input_characters_matrix[0])

        possible_row_indices = []
        possible_column_indices = []

        for k in [-1, 0, 1]:
            if not (i + k < 0 or i + k >= max_rows):
                possible_row_indices.append(i + k)

            if not (j + k < 0 or j + k >= max_columns):
                possible_column_indices.append(j + k)

        possible_neighbors = [(x, y) for x in possible_row_indices for y in possible_column_indices]

        for (neighbor_i, neighbor_j) in possible_neighbors:
            if (neighbor_i, neighbor_j) != (i, j):
                graph.add_edge(max_rows * i + j,
                               max_rows * neighbor_i + neighbor_j)

    def get_characters_list(self):
        """Create an one-to-one mapping of boggle board to a list

        Args:

        Returns:
            list

        Raises:
            None
        """
        max_rows = len(self.input_characters_matrix)
        max_columns = len(self.input_characters_matrix[0])
        characters_list = []
        for i in range(max_rows):
            for j in range(max_columns):
                characters_list.append(self.input_characters_matrix[i][j])

        return characters_list
