class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # O(1) time complexity solution
        # Extract the first two edges
        edge1, edge2 = edges[0], edges[1]

        # Check if the first node of edge1 is in edge2; if yes, it's the center.
        # Otherwise, the second node of edge1 is the center.
        if edge1[0] in edge2:
            return edge1[0]
        else:
            return edge1[1]

        # O(n) time complexity
        # nodes = {}
        # for edge in edges:
        #     n1, n2 = edge
        #     nodes[n1] = nodes.get(n1, 0) + 1
        #     nodes[n2] = nodes.get(n2, 0) + 1
        #     # If any node reaches the count of len(edges), it's the center
        #     if nodes[n1] == len(edges):
        #         return n1
        #     if nodes[n2] == len(edges):
        #         return n2
