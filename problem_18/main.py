

# Define the structure for a graph node
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.next_nodes = [None, None]

class Solution:
    def __init__(self, data_file):
        self.graph_root = None
        self.init_graph(data_file)

    def init_graph(self, data_file):
        """
        Convert the triangle data to a graph
        """
        with open(data_file, "r") as f:
            parent_line_nodes = []
            for line in f: 
                numbers = [int(n) for n in line.replace('\r', '').replace('\n', '').split(' ')]
                if len(parent_line_nodes) ==0: 
                    self.graph_root = GraphNode(numbers[0])  # first line --> create root node
                    current_line_nodes = [self.graph_root]
                else:  # not the first line, create nodes and attach them to parent nodes
                    current_line_nodes = [GraphNode(n) for n in numbers]
                    for i in range(len(parent_line_nodes)):
                        parent_line_nodes[i].next_nodes = [current_line_nodes[i], current_line_nodes[i+1]]
                parent_line_nodes = current_line_nodes
                

    def print_graph(self):
        pass

    def max_path_sum(self):
        """
        Do a recursive DFS 
        """
        
        # Max path sum helper function
        def mps(root_node):
            if root_node is None:
                return 0
            else:
                return root_node.val + max(mps(root_node.next_nodes[0]), mps(root_node.next_nodes[1]))
        return mps(self.graph_root)


if __name__ == "__main__":
    #s = Solution('triangle_test.txt')
    s = Solution('triangle.txt')
    print s.max_path_sum()


