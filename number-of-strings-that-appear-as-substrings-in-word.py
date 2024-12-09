class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(1 for substring in patterns if substring in word)
