"""
Clone Graph (Depth First)

Clone an undirected graph. Each node in the graph contains a label and a list of its
neighbors.
"""
from common.graph import GraphNode
from common.problem import Problem
from common.stack import Stack


class CloneGraphDepthFirst(Problem):
    """
    Clone Graph (Depth First)
    """
    PROBLEM_NAME = "CloneGraphDepthFirst"

    def __init__(self, input_graph_node):
        """Clone Graph (Depth First)

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

        Note: O(n) (runtime) and O(n) (space) solution uses the depth  first traversal to traverse nodes and copy node neighbors.

        Args:

        Returns:
            GraphNode

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        # Create a stack for DFS
        nodes_stack = Stack()
        nodes_stack.push(self.input_graph_node)

        # Root node to return for the cloned graph
        cloned_graph_node = GraphNode(self.input_graph_node.data)

        # Bookkeeping visited nodes -- contains the cloned nodes
        visited_dict = {self.input_graph_node: cloned_graph_node}

        while len(nodes_stack) > 0:
            current_node = nodes_stack.pop()
            copied_node = visited_dict[current_node]

            # iterate current node's neighbors
            for node in current_node.neighbors:
                # if the node is already not visited
                if node not in visited_dict:
                    # append the node to queue
                    nodes_stack.push(node)

                    # create a copy node for the neighbor
                    neighbor_node = GraphNode(node.data)

                    # add neighbor and update visited
                    copied_node.add_neighbor(neighbor_node)
                    visited_dict[node] = neighbor_node
                else:
                    # if the node is already visited
                    neighbor_node = visited_dict[node]

                    # Add the neighbor node to the copied node's neighbors if it's not added
                    if neighbor_node not in copied_node.neighbors:
                        copied_node.add_neighbor(neighbor_node)

        return cloned_graph_node
