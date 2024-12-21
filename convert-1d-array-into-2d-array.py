class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        length = len(original)

        # Check if the transformation is possible
        if m * n != length:
            return []

        # Construct the 2D array
        twoDArray = []
        for i in range(0, length, n):
            twoDArray.append(original[i : i + n])

        return twoDArray
