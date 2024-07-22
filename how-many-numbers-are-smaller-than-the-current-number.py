class Solution:
    """
    def smallerNumbersThanCurrent(nums):
        # Initialize the result list
        result = []

        # Iterate through each element in nums
        for i in range(len(nums)):
            count = 0
            # Compare with every other element
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    count += 1
            # Append the count to the result list
            result.append(count)

        return result
    """

    # Optimized solution

    def smallerNumbersThanCurrent(nums):
        sorted_nums = sorted(nums)
        result = []

        # Create a dictionary to store the number of elements smaller than each number
        smaller_count = {}

        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in smaller_count:
                smaller_count[sorted_nums[i]] = i

        for num in nums:
            result.append(smaller_count[num])

        return result
