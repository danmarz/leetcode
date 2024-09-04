class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # Initialize a counter to track consecutive odd numbers
        count = 0

        # Loop through the array to check each number
        for num in arr:
            # Check if the current number is odd
            if num % 2 != 0:
                # Increment the counter if the number is odd
                count += 1
            else:
                # Reset the counter to 0 if the number is even
                count = 0

            # If we find three consecutive odd numbers, return True
            if count == 3:
                return True

        # If we finish the loop and don't find three consecutive odds, return False
        return False

        # # Bruteforce alternative
        # for pos in range(len(arr) - 2):
        #     if arr[pos] % 2 != 0 and arr[pos + 1] % 2 != 0 and arr[pos + 2] % 2 != 0:
        #         return True
        # return False
