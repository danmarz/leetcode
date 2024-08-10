class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing_cities = set()

        # Add all cities that have an outgoing path to the set
        for path in paths:
            outgoing_cities.add(path[0])

        # The destination city will be the one that is not in the outgoing_cities set
        for path in paths:
            if path[1] not in outgoing_cities:
                return path[1]
