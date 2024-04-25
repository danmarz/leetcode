class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Find the lengths of str1 and str2
        len1, len2 = len(str1), len(str2)

        # Find the greatest common divisor of len1 and len2
        while len2:
            len1, len2 = len2, len1 % len2
            print(len1, len2)

        # Check if the common prefix of str1 and str2 is a divisor of both strings
        prefix = str1[:len1]
        if str1 == prefix * (len(str1) // len1) and str2 == prefix * (
            len(str2) // len1
        ):
            return prefix
        else:
            return ""
