class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        n = len(word)
        res = 0

        for i in range(n):
            s = set()
            for ch in word[i:]:
                if ch not in vowels:
                    break
                s.add(ch)
                if len(s) == 5:
                    res += 1

        return res
