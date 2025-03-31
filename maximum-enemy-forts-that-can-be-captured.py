class Solution:
    def captureForts(self, forts: List[int]) -> int:
        max_captures = 0
        last = -1  # to store the index of the last non-zero fort (-1 or 1)

        for i in range(len(forts)):
            if forts[i] != 0:
                if last != -1 and forts[i] != forts[last]:
                    # Check if the segment between last and current is all enemy forts
                    # That happens because we are only updating `last` on non-zero forts
                    max_captures = max(max_captures, abs(i - last) - 1)
                last = i  # Update last seen non-zero fort

        return max_captures
