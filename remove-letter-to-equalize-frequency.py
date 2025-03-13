class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            new_word = word[:i] + word[i + 1:]
            count = Counter(new_word)
            if len(set(Counter(new_word).values())) == 1:
                return True
        return False
