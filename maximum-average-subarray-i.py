class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculate the length of the input array
        n = len(nums)

        # Calculate the sum of the first k elements
        current_sum = sum(nums[:k])
        # Initialize max_sum with the sum of the first k elements
        max_sum = current_sum

        # Iterate through the array starting from index k
        for i in range(k, n):
            # Update the sum by subtracting the element that goes out of the window and adding the new element
            current_sum = current_sum - nums[i - k] + nums[i]
            # Update max_sum if the current sum is greater
            max_sum = max(max_sum, current_sum)

        # Calculate the average value by dividing max_sum by k
        max_average = max_sum / k

        return max_average
