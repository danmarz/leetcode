class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Initialize two pointers, one for iterating and one for placing non-zeros.
        slow = 0

        # Iterate through the array with the fast pointer.
        for fast in range(len(nums)):
            if nums[fast] != 0:
                # If the current element is non-zero, move it to the slow pointer's position.
                nums[slow] = nums[fast]
                # Increment the slow pointer.
                slow += 1

        # After processing all elements, fill the remaining positions with zeros.
        for i in range(slow, len(nums)):
            nums[i] = 0

        """ Solution 2 (much slower):

        for i in range(len(nums)):
            print(nums[i])
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                
        """
