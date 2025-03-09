class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even_nums = defaultdict(int)

        for num in nums:
            if num % 2 == 0:
                even_nums[num] += 1

        if not even_nums:
            return -1

        # Find the maximum value
        max_value = max(even_nums.values())

        # Extract all keys with the maximum value
        max_keys = [key for key, value in even_nums.items() if value == max_value]

        # Return the smallest (even) dict key
        return min(max_keys)
