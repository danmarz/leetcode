class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = float("inf")
        min_index = -1

        for i, (a, b) in enumerate(points):
            # Check if the point is valid
            if a == x or b == y:
                # Calculate Manhattan distance
                distance = abs(x - a) + abs(y - b)
                # Update minimum distance and index if this distance is smaller
                if distance < min_distance:
                    min_distance = distance
                    min_index = i
                # If the distance is the same but index is smaller, choose the smaller index
                elif distance == min_distance and i < min_index:
                    min_index = i

        return min_index
