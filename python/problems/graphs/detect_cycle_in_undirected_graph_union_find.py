"""
Given an undirected graph, how to check if there is a cycle in the graph?

For example,

1----2
| \  |
|  \ |
4----3

Has a cycle. 1->2->3->1

Note: Use Union Find dataStructure to detect cycles.

"""
from common.problem import Problem
from common.unionfind import UnionFind


class DetectCycleInUndirectedGraphUnionFind(Problem):
    """
    Detect Cycle in a Undirected Graph (Union Find)
    """
    PROBLEM_NAME = "DetectCycleInUndirectedGraphUnionFind"

    def __init__(self, input_graph):
        """Detect Cycle in a Undirected Graph (Union Find)

        Args:
            input_graph: Graph

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_graph = input_graph

    def solve(self):
        """Solve the problem

        Note:

        Args:

        Returns:
            Boolean

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        vertices = self.input_graph.get_vertices()

        parent_list = [i for i in vertices]

        union_find = UnionFind(parent_list)

        for vertex in vertices:
            for neighbor in self.input_graph.get_neighbors(vertex):
                vertex_parent = union_find.find(vertex)
                neighbor_parent = union_find.find(neighbor)

                # They both have the same parents, should be a cycle
                if vertex_parent == neighbor_parent:
                    return True
                else:
                    union_find.union(vertex, neighbor)

        return False
