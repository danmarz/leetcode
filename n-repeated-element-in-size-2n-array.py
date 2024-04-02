class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # Initialize an empty dictionary to store the frequency of each element
        counter = {}

        # Iterate through each element in nums
        for num in nums:
            # If the element is not already in the dictionary, add it with count 1
            # If the element is already in the dictionary, increment its count by 1
            counter[num] = counter.get(num, 0) + 1

        # Iterate through the items in the dictionary
        for num, count in counter.items():
            # If the count of the element is equal to n, return that element
            if count == len(nums) // 2:
                return num
