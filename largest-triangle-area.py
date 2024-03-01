class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # Function to calculate the area of a triangle given three points
        def area(x1, y1, x2, y2, x3, y3):
            return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

        # Initialize variable to store the maximum area
        max_area = 0

        # Iterate over all combinations of three points
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    # Get the coordinates of the three points
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    # Calculate the area of the triangle formed by the three points
                    curr_area = area(x1, y1, x2, y2, x3, y3)
                    # Update the maximum area if the current area is greater
                    max_area = max(max_area, curr_area)

        # Return the maximum area
        return max_area
