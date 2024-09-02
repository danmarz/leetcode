class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # # Solution 1: Binary Search Approach
        # # Initialize binary search bounds
        # left, right = 0, len(arr)

        # # Perform binary search
        # while left < right:
        #     mid = (left + right) // 2
        #     # Calculate the number of missing integers before arr[mid]
        #     missing = arr[mid] - (mid + 1)

        #     if missing < k:
        #         # If the number of missing numbers up to arr[mid] is less than k,
        #         # search in the right half
        #         left = mid + 1
        #     else:
        #         # Otherwise, search in the left half
        #         right = mid

        # # After the loop, left is the first index where the number of missing numbers
        # # exceeds or equals k, so the kth missing number is to the left of arr[left]
        # return left + k

        # Solution 2: Linear Scan Approach
        # Initialize the variable to track the number of missing integers
        missing_count = 0
        # Initialize a pointer to iterate through the array
        index = 0

        # Iterate through numbers starting from 1 upwards
        current_number = 1
        while True:
            print(index, current_number)
            if index < len(arr) and arr[index] == current_number:
                # If the current number is in the array, move to the next number in the array
                index += 1
            else:
                # If the current number is not in the array, it's a missing number
                print(current_number, "was missing.")
                missing_count += 1
                # If we've found the kth missing number, return it
                if missing_count == k:
                    return current_number
            # Move to the next number
            current_number += 1
