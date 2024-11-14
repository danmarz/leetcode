class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        # min_abs = -1
        # for pos, num in enumerate(nums):
        #     if num == target:
        #         if min_abs == -1:
        #             min_abs = abs(pos - start)
        #         else:
        #             min_abs = min(min_abs, abs(pos - start))
        # return min_abs

        # Optimized approach, simplify the comparison by using infinity & early exit if 0
        min_abs = float("inf")  # Use infinity to simplify the comparison
        for pos, num in enumerate(nums):
            if num == target:
                min_abs = min(min_abs, abs(pos - start))
                if (
                    min_abs == 0
                ):  # Early exit if the smallest possible distance is found
                    break
        return min_abs
