class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""

        sortedList = sorted(strs)
        first = sortedList[0]
        last = sortedList[-1]

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return common
            common += first[i]

        return common


# Alternative solution (try/except block with IndexError)
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            sym = strs[0][i]

            for s in strs:
                try:
                    if s[i] != sym:
                        return strs[0][:i]
                except IndexError:
                    return strs[0][:i]
        return strs[0]
"""
