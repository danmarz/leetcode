class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words
        words = s.split()

        # Reverse each word and join them back pythonically
        reversed_words = [word[::-1] for word in words]

        return " ".join(reversed_words)

        # Dinosaur approach
        """
        for pos,word in enumerate(words):
            words[pos] = word[::-1]

        return ' '.join(words)
        """
