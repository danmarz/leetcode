class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            index = word.index(ch) + 1
            # word = ''.join(reversed(word[:index])) + word[index:]
            word = (
                word[:index][::-1] + word[index:]
            )  # Reversing the prefix using slicing is 3 times faster, at least
        return word
