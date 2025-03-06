class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # Step 1: Sort nums to prioritize smaller numbers
        nums.sort()

        # Step 2: Compute prefix sum array
        prefix = [0] * len(nums)
        prefix[0] = nums[0]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]

        # Step 3: Answer each query using binary search
        result = []
        for q in queries:
            # Find the maximum subsequence length with sum <= q
            idx = bisect_right(prefix, q)  # Returns index where q would fit
            result.append(idx)  # idx represents the count of elements we can take

        return result
