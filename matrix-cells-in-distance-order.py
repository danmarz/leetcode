class Solution:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> List[List[int]]:
        distances = []  # List to store tuples of (distance, coordinates)

        # Iterate through all cells in the matrix
        for r in range(rows):
            for c in range(cols):
                # Calculate the Manhattan distance between the current cell and the center cell
                distance = abs(r - rCenter) + abs(c - cCenter)
                # Append a tuple of (distance, coordinates) to the distances list
                distances.append((distance, (r, c)))

        # Sort the distances list based on the distance (first element of each tuple)
        distances.sort()

        # Extract and return the coordinates from the sorted distances list
        return [coord for distance, coord in distances]
