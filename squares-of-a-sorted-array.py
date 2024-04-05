class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Initialize an array to store the squares of each number
        squares = []

        # Initialize pointers for the start and end of the array
        left, right = 0, len(nums) - 1

        # Iterate through the array from right to left
        while left <= right:
            # Compare the absolute values of the elements at the start and end
            if abs(nums[left]) > abs(nums[right]):
                # If the absolute value of the element at the start is greater,
                # append its square to the squares array and move the left pointer forward
                squares.append(nums[left] ** 2)
                left += 1
            else:
                # If the absolute value of the element at the end is greater or equal,
                # append its square to the squares array and move the right pointer backward
                squares.append(nums[right] ** 2)
                right -= 1

        # Return the squares array sorted in non-decreasing order
        return squares[::-1]