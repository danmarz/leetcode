class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def contains_zero(x):
            return "0" in str(x)

        a = 1
        b = n - a

        while contains_zero(a) or contains_zero(b):
            a += 1
            b = n - a  # Recalculate b based on the new a

        return [a, b]
