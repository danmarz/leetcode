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
