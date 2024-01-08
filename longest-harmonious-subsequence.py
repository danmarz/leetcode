class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Create a dictionary to store the count of each unique number in the input list
        count = {}
        # Variable to keep track of the longest harmonious subsequence found
        result = 0

        # Count the frequency of each number in the input list
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Iterate through the keys in the count dictionary
        for key in count:
            # Check if the next number in sequence (key + 1) exists in the count
            if key + 1 in count:
                # Calculate the length of the harmonious subsequence and update result if it's longer
                result = max(result, count[key] + count[key + 1])

        # Return the length of the longest harmonious subsequence found
        return result
