class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # Preferred approach using Counter class from collections library
        from collections import Counter

        count = 0
        freq = Counter()

        for num in nums:
            # Check for complement pairs
            count += freq[num - k] + freq[num + k]
            # Update the frequency map
            freq[num] += 1

        return count

        # # Alternative to Counter by using a dict and explicitly handling key check's and initialization
        # f = {}
        # count = 0

        # for i in range(len(nums)):

        #     if nums[i] - k in f:
        #         count += f[nums[i] - k]
        #     if nums[i] + k in f:
        #         count += f[nums[i] + k]

        #     if nums[i] not in f:
        #         f[nums[i]] = 1
        #     else:
        #         f[nums[i]] += 1

        # return count

        # # Nested loops beginner approach:

        # seen = 0
        # for n1 in range(len(nums)):
        #     for n2 in range(n1 + 1, len(nums)):
        #         if abs(nums[n1] - nums[n2]) == k:
        #             seen += 1
        # return seen
