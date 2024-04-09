class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # Find the position of the white rook 'R'
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    rook_row, rook_col = i, j
                    break

        # Define directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Initialize the number of captured pawns
        captures = 0

        # Check in each direction for black pawns
        for dr, dc in directions:
            row, col = rook_row + dr, rook_col + dc
            while 0 <= row < 8 and 0 <= col < 8:
                if (
                    board[row][col] == "B"
                ):  # If a bishop blocks the path, stop searching in this direction
                    break
                if (
                    board[row][col] == "p"
                ):  # If a black pawn is found, increment the captures count
                    captures += 1
                    break
                row += dr
                col += dc

        return captures
