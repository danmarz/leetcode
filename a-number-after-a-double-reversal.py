class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # def reverse_n(n):
        #     return int(str(n)[::-1])

        # return reverse_n(reverse_n(num)) == num

        # Mathematical insight: Zero is always true; and numbers without trailing zeros will remain unchanged
        return num == 0 or num % 10 != 0
