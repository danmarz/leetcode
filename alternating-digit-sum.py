class Solution:
    def alternateDigitSum(self, n: int) -> int:
        str_n = str(n)
        digits = 0
        for i in range(len(str_n)):
            if i % 2 == 0:
                digits += int(str_n[i])
            else:
                digits -= int(str_n[i])
        return digits
