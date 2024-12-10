class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        # # DFS (with recursion)
        # def validPath(n, edges, source, destination):
        #     neighbors = defaultdict(list)
        #     for v1, v2 in edges:
        #         neighbors[v1].append(v2)
        #         neighbors[v2].append(v1)

        #     # DFS function
        #     def dfs(node, visited):
        #         if node == destination:
        #             return True
        #         visited.add(node)
        #         for neighbor in neighbors[node]:
        #             if neighbor not in visited:
        #                 if dfs(neighbor, visited):
        #                     return True
        #         return False

        #     # Start DFS
        #     visited = set()
        #     return dfs(source, visited)

        # return validPath(n, edges, source, destination)

        # # DFS (with a stack)
        # def validPath(n, edges, source, destination):
        #     # Create an adjacency list
        #     adj_list = defaultdict(list)
        #     for u, v in edges:
        #         adj_list[u].append(v)
        #         adj_list[v].append(u)

        #     # Use an explicit stack for DFS
        #     stack = [source]
        #     visited = set()

        #     while stack:
        #         node = stack.pop()
        #         if node == destination:
        #             return True
        #         if node not in visited:
        #             visited.add(node)
        #             for neighbor in adj_list[node]:
        #                 if neighbor not in visited:
        #                     stack.append(neighbor)

        #     return False
        # return validPath(n, edges, source, destination)

        # BFS alternative (queue)
        def validPath(n, edges, source, destination):
            # Create an adjacency list
            adj_list = defaultdict(list)
            for u, v in edges:
                adj_list[u].append(v)
                adj_list[v].append(u)  # Because the graph is bidirectional

            # BFS
            queue = deque([source])
            visited = set([source])

            while queue:
                node = queue.popleft()
                if node == destination:
                    return True

                for neighbor in adj_list[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            return False

        return validPath(n, edges, source, destination)
