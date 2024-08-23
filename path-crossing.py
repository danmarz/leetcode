class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Initialize the starting position at the origin (0, 0)
        x, y = 0, 0

        # Create a set to keep track of visited positions
        visited_positions = set()

        # Add the origin to the set of visited positions
        visited_positions.add((x, y))

        # Iterate over each direction in the path string
        for direction in path:
            # Update the current position based on the direction
            if direction == "N":  # Move north
                y += 1
            elif direction == "S":  # Move south
                y -= 1
            elif direction == "E":  # Move east
                x += 1
            elif direction == "W":  # Move west
                x -= 1

            # Create a tuple of the current position
            current_position = (x, y)

            # Check if this position has already been visited
            if current_position in visited_positions:
                # If yes, the path crosses itself, so return True
                return True

            # Otherwise, add the current position to the set of visited positions
            visited_positions.add(current_position)

        # If the loop completes without finding any crossing, return False
        return False
