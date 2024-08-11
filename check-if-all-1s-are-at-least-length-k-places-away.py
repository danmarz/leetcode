class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev_index = -1  # To store the index of the previous 1

        for i in range(len(nums)):
            if nums[i] == 1:
                if prev_index != -1 and i - prev_index - 1 < k:
                    return False
                prev_index = i

        return True
