class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0  # Pointer starting from the beginning of the array
        right = len(nums) - 1  # Pointer starting from the end of the array

        while left < right:
            if nums[left] % 2 == 0:  # Even number found
                left += 1
            elif nums[right] % 2 != 0:  # Odd number found
                right -= 1
            else:
                # Swap the even number at nums[left] with the odd number at nums[right]
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums
