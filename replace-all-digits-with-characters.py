class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c, x):
            return chr(ord(c) + x)

        res = []
        for i in range(len(s)):
            if i % 2 != 0:
                res.append(shift(s[i - 1], int(s[i])))
            else:
                res.append(s[i])

        return "".join(res)
