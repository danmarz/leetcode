class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = s.count(letter)
        if count:
            return int(count / len(s) * 100)
        else:
            return 0
