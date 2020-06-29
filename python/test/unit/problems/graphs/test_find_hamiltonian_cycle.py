"""
Unit Test for detect_cycle_in_undirected_graph
"""
from unittest import TestCase

from common.graph import UndirectedGraph
from problems.graphs.find_hamiltonian_cycle import FindHamiltonianCycle


class TestFindHamiltonianCycle(TestCase):
    """
    Unit test for FindHamiltonianCycle
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestFindHamiltonianCycle

        Returns:
            None

        Raises:
            None
        """
        # Given
        '''
        Note : All the edges are Undirected 
        Given Graph: 
        0--1 
        | | 
        3--2 
        '''
        graph = UndirectedGraph()
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 0)

        hamiltonian_cycle_problem = FindHamiltonianCycle(graph)

        # When
        result = hamiltonian_cycle_problem.solve()

        # Then
        self.assertEqual(result, [0, 1, 2, 3])

    def test_solve_not_cycle(self):
        """Test solve (not cycle)

        Args:
            self: TestFindHamiltonianCycle

        Returns:
            None

        Raises:
            None
        """
        # Given
        '''
        Note : All the edges are Undirected 
        Given Graph: 
        0--1 
        | | 
        3 2 
        '''
        graph = UndirectedGraph()
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        # graph.add_edge(2, 3)
        graph.add_edge(3, 0)

        hamiltonian_cycle_problem = FindHamiltonianCycle(graph)

        # When
        result = hamiltonian_cycle_problem.solve()

        # Then
        self.assertEqual(result, [])
