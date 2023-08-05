class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Solution 1
        """
        count = nums.count(val)
        for i in range(count):
            nums.remove(val)
        """

        # Solution 2
        """
        nums[:] = [i for i in nums if i != val]
        """

        # Solution 3
        while val in nums:
            nums.remove(val)

        return len(nums)
