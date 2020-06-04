"""
Is Graph Bipartite

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

Example:

0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.

0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
"""
from common.problem import Problem
from common.stack import Stack


class IsGraphBipartite(Problem):
    """
    Is Graph Bipartite
    """
    PROBLEM_NAME = "IsGraphBipartite"
    NODE_COLOR_RED = "RED"
    NODE_COLOR_BLUE = "BLUE"
    NODE_COLORS = {NODE_COLOR_RED, NODE_COLOR_BLUE}

    def __init__(self, input_graph_node):
        """Is Graph Bipartite

        Args:
            input_graph_node: Graph node
        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_graph_node = input_graph_node

    def solve(self):
        """Solve the problem

        Note: O(n) solution works by using the depth first search to color nodes.
        If the node color and the neighbor's color are the same, it's not a bipartite.

        Args:

        Returns:
            Boolean

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        nodes_stack = Stack()
        nodes_stack.push(self.input_graph_node)

        visited_vertex_list = []
        visited_node_color_dict = {self.input_graph_node: self.NODE_COLOR_RED}

        # iterate through the node stack and check for visited nodes and add the non-visited nodes.
        while len(nodes_stack) > 0:
            node = nodes_stack.pop()
            node_color = visited_node_color_dict[node]
            neighbor_color = (self.NODE_COLORS - {node_color}).pop()

            if node not in visited_vertex_list:
                visited_vertex_list.append(node)

                for neighbor_node in node.neighbors:
                    nodes_stack.push(neighbor_node)

                    if neighbor_node not in visited_node_color_dict:
                        visited_node_color_dict[neighbor_node] = neighbor_color
                    else:
                        actual_neighbor_color = visited_node_color_dict[neighbor_node]

                        if actual_neighbor_color != neighbor_color:
                            return False

        return True
