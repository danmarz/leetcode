class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_value = 0
        for s in strs:
            if s.isnumeric():
                value = int(s)
            else:
                value = len(s)
            max_value = max(value, max_value)
        return max_value
