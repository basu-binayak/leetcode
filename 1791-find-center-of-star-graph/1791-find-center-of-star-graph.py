class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # The center node of a star graph will have a degree equal 
        # to n-1, as it is connected to all other nodes. So, you can
        # simply iterate through the given edges and count the degrees
        # of each node. The node with a degree of n - 1 will be the
        # center of the star graph.

        # Initialize a dictionary to store the degree of each node
        degree_count = {}

        # Iterate through the edges and count the degree of each node
        for edge in edges:
            u, v = edge
            degree_count[u] = degree_count.get(u, 0) + 1
            degree_count[v] = degree_count.get(v, 0) + 1
        
        # Find the node with a degree of n - 1 (the center node)
        for node, degree in degree_count.items():
            if degree == len(degree_count.keys())-1:
                return node



        





