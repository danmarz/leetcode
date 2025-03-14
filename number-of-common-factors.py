class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        result = 0
        if a > b:
            for i in range(1, b + 1):
                if a % i == 0 and b % i == 0:
                    result += 1
        else:
            for i in range(1, a + 1):
                if a % i == 0 and b % i == 0:
                    result += 1
        return result
