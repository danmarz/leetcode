class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        # Step 1: Calculate the total sum of the array
        total_sum = sum(arr)

        # Step 2: Check if the total sum is divisible by 3
        if total_sum % 3 != 0:
            return False  # If not divisible by 3, return False

        # Step 3: Initialize variables to track sum and count of partitions
        target_sum = total_sum // 3  # Each partition should have this sum
        partition_sum = 0
        partition_count = 0

        # Step 4: Iterate through the array to find partition points
        for num in arr:
            partition_sum += num
            if partition_sum == target_sum:
                partition_sum = 0  # Reset partition sum
                partition_count += 1

        # Step 5: Check if we found exactly three partitions
        return partition_count >= 3
