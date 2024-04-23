class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Initialize count of mismatches
        mismatches = 0
        expected = sorted(heights)

        # Iterate through both arrays simultaneously
        for height, exp_height in zip(heights, expected):
            # If the heights differ, increment the count of mismatches
            if height != exp_height:
                mismatches += 1

        return mismatches
