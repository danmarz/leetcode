class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # Step 1: Handle edge cases
        if len(points) <= 1:
            return 0

        # Step 2: Extract all the x-coordinates from the points
        x_coords = [
            x for x, y in points
        ]  # equivalent to: x_coords = [x[0] for x in points]

        # Another edge case: check if all x-coordinates are the same, return 0 if so
        if len(set(x_coords)) == 1:
            return 0

        # Step 3: Sort the x-coordinates
        x_coords.sort()

        # Step 4: Compute the maximum difference between consecutive x-coordinates
        max_width = 0
        for i in range(1, len(x_coords)):
            max_width = max(max_width, x_coords[i] - x_coords[i - 1])

        return max_width
