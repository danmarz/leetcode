class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = Counter(s)
        for letter in letters:
            if letters[letter] == 1:
                return s.index(letter)
        return -1

        """ Alternative using enumerate()
        counter = Counter(s)
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i
            
        return -1
        """
