class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Check if all points lie on a straight line
        # Calculate the slope of the line formed by the first two points
        slope = (
            (coordinates[1][1] - coordinates[0][1])
            / (coordinates[1][0] - coordinates[0][0])
            if coordinates[1][0] != coordinates[0][0]
            else float("inf")
        )

        # Iterate through the remaining points to check if they lie on the same line
        for i in range(2, len(coordinates)):
            # Calculate the slope of the line formed by the current point and the first point
            current_slope = (
                (coordinates[i][1] - coordinates[0][1])
                / (coordinates[i][0] - coordinates[0][0])
                if coordinates[i][0] != coordinates[0][0]
                else float("inf")
            )
            # If the slopes are different, return False
            if current_slope != slope:
                return False

        # If all points lie on the same line, return True
        return True
