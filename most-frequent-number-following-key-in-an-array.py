class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        freq = defaultdict(int)
        for i in range(len(nums) - 1):
            if nums[i] == key:
                freq[nums[i + 1]] += 1
        return max(freq, key=freq.get)
