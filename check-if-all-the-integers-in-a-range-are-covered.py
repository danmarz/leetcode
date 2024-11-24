class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left, right + 1):
            # Check if `num` is covered by any range
            covered = False
            for start, end in ranges:
                if start <= num <= end:
                    covered = True
                    break  # No need to check other ranges for this number
            if not covered:  # If any number is uncovered, return False
                return False

        return True  # All numbers are covered
