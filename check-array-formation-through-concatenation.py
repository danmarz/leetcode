class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # Create a dictionary that maps the first element of each piece to the piece
        piece_map = {p[0]: p for p in pieces}

        i = 0
        while i < len(arr):
            # Check if arr[i] is the start of a piece
            if arr[i] not in piece_map:
                return False

            # Get the corresponding piece
            piece = piece_map[arr[i]]

            # Check if the next part of arr matches this piece
            if arr[i : i + len(piece)] != piece:
                return False

            # Move the index forward by the length of the current piece
            i += len(piece)

        return True
