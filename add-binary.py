class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = str(bin(int(a, 2) + int(b, 2)))
        return sum[2:]
