class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Solution 1
        """
        try:
            index = haystack.index(needle)
        except ValueError:
            index = -1
        return index
        """

        # Solution 2
        """
        for i in range(len(haystack)):
            if needle[0]==haystack[i]:
                if needle[0:]==haystack[i:i+len(needle)]:
                    return i
                else:
                    continue
        return -1
        """

        # Solution 3
        for i in range(len(haystack) - len(needle) + 1):
            if all(haystack[i + j] == needle[j] for j in range(len(needle))):
                return i
        return -1
