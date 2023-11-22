class Solution:
    def findComplement(self, num: int) -> int:
        num = str(bin(num))[2:]
        ans = ""

        for char in num:
            if int(char) == 0:
                ans += "1"
            else:
                ans += "0"

        return int(ans, 2)
