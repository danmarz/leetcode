class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # Initialize counters for even and odd positions
        even_count = 0
        odd_count = 0

        # Iterate through each position in the list
        for pos in position:
            # Check if the position is even
            if pos % 2 == 0:
                even_count += 1  # Increment even count
            else:
                odd_count += 1  # Increment odd count

        # Return the minimum of even and odd counts
        return min(even_count, odd_count)
