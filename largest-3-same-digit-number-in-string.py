class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good = []
        for i in range(len(num) - 2):
            good_test = num[i : i + 3]
            if len(set(good_test)) == 1:
                good.append(good_test)

        if not good:
            return ""

        return max(good)

        # # Optimized, one liner:
        # return max((num[i] * 3 for i in range(len(num) - 2) if num[i] == num[i+1] == num[i+2]), default="")
