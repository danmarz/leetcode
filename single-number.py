class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        checklist = []
        for num in nums:
            if num not in checklist:
                checklist.append(num)
            else:
                checklist.remove(num)
        return checklist[0]
        """

        # XOR bitwise solution
        digit = 0
        for n in nums:
            digit = digit ^ n
        return digit
