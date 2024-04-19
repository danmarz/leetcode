class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # Check if any two points are equal
        if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]:
            return False

        # Unpack the points
        (x1, y1), (x2, y2), (x3, y3) = points

        # Calculate the slopes
        slope1 = (y2 - y1) * (x3 - x2)
        slope2 = (y3 - y2) * (x2 - x1)

        # Check if slopes are not equal (not collinear)
        return slope1 != slope2
