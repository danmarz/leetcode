class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        # leftovers = []
        # pairs = 0

        # for n in nums:
        #     if n not in leftovers:
        #         leftovers.append(n)
        #     else:
        #         pairs += 1
        #         leftovers.pop(leftovers.index(n))

        # return [pairs, len(leftovers)]

        # Alternative using Counter
        num_counts = Counter(nums)
        pairs = 0
        leftovers = 0

        for count in num_counts.values():
            pairs += count // 2  # Count pairs
            leftovers += count % 2  # Count leftovers

        return [pairs, leftovers]
