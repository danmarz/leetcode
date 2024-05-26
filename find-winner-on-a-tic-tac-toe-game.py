class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # Initialize a 3x3 board
        board = [["" for _ in range(3)] for _ in range(3)]

        # Place 'X' and 'O' on the board according to the moves
        for i, move in enumerate(moves):
            player = "X" if i % 2 == 0 else "O"
            row, col = move
            board[row][col] = player

            # Check if the current player has won
            if (
                board[row][0] == board[row][1] == board[row][2] == player  # Row
                or board[0][col] == board[1][col] == board[2][col] == player  # Column
                or board[0][0] == board[1][1] == board[2][2] == player  # Diagonal
                or board[0][2] == board[1][1] == board[2][0] == player
            ):  # Anti-diagonal
                return "A" if player == "X" else "B"

        # If all moves are played and no winner
        if len(moves) == 9:
            return "Draw"

        # If there are still moves left
        return "Pending"
