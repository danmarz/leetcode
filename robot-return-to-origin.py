class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Simple solution using count()
        if moves.count("U") == moves.count("D") and moves.count("L") == moves.count(
            "R"
        ):
            return True
        return False

        # Alternative solution
        """
        # Initialize counters for horizontal and vertical movements
        horizontal = 0
        vertical = 0
        
        # Iterate through each move in the sequence
        for move in moves:
            if move == 'U':
                vertical += 1  # Move up
            elif move == 'D':
                vertical -= 1  # Move down
            elif move == 'L':
                horizontal -= 1  # Move left
            elif move == 'R':
                horizontal += 1  # Move right
        
        # Check if the final position is at the origin (0, 0)
        return horizontal == 0 and vertical == 0
        """
