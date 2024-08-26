class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Dictionary to store the frequency of each number in nums
        freq = {}
        # Variable to count the number of good pairs
        pairs = 0

        # Iterate through each number in the array
        for num in nums:
            # If the number has been seen before
            if num in freq:
                # Add the current frequency of the number to pairs
                # This accounts for all the good pairs that can be formed with previous occurrences of num
                pairs += freq[num]
                # Increment the frequency of the number
                freq[num] += 1
            else:
                # If the number is seen for the first time, set its frequency to 1
                freq[num] = 1

        # Return the total count of good pairs
        return pairs

        # # Nested loops approach, quite inefficient as it needs to iterate through the nums array twice for every item O(n^2)
        # pairs = 0

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             pairs += 1

        # return pairs
