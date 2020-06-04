"""
Clone Graph (Breadth First)

Clone an undirected graph. Each node in the graph contains a label and a list of its
neighbors.
"""
from collections import deque

from common.graph import GraphNode
from common.problem import Problem


class CloneGraphBreadthFirst(Problem):
    """
    Clone Graph (Breadth First)
    """
    PROBLEM_NAME = "CloneGraphBreadthFirst"

    def __init__(self, input_graph_node):
        """Clone Graph (Breadth First)

        Args:
            input_graph_node: A graph node

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_graph_node = input_graph_node

    def solve(self):
        """Solve the problem

        Note: O(n) (runtime) and O(n) (space) solution uses the breadth first traversal to traverse nodes and copy node neighbors.

        Args:

        Returns:
            GraphNode

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        # Create a queue for BFS
        nodes_queue = deque()
        nodes_queue.append(self.input_graph_node)

        # Root node to return for the cloned graph
        cloned_graph_node = GraphNode(self.input_graph_node.data)

        # Bookkeeping visited nodes -- contains the cloned nodes
        visited_dict = {self.input_graph_node: cloned_graph_node}

        while len(nodes_queue) > 0:
            current_node = nodes_queue.popleft()
            copied_node = visited_dict[current_node]

            # iterate current node's neighbors
            for node in current_node.neighbors:
                # if the node is already not visited
                if node not in visited_dict:
                    # append the node to queue
                    nodes_queue.append(node)

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
