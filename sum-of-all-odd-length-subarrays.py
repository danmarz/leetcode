class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sum = 0  # Initialize the total sum of odd-length subarrays

        # Iterate over each element in the array
        for i in range(len(arr)):
            # We need to count the contribution of each element to all odd-length subarrays
            # Each element arr[i] belongs to subarrays that start before it and end after it.
            # The number of subarrays that include arr[i] is (i+1) * (len(arr) - i)
            # Out of these subarrays, half (rounded up) will have an odd length.

            # Calculate the number of subarrays starting before or at 'i' and ending after 'i'
            start_count = i + 1
            end_count = len(arr) - i

            # Total subarrays that include arr[i]
            total_subarrays = start_count * end_count

            # Only half of these subarrays will have odd lengths. We use (total_subarrays + 1) // 2
            # to count the odd-length subarrays.
            odd_subarrays = (total_subarrays + 1) // 2

            # Add the contribution of arr[i] to the total sum
            total_sum += arr[i] * odd_subarrays

        return total_sum  # Return the final total sum of odd-length subarrays
