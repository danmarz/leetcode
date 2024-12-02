class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = 0
        for word in text.split():
            for key in brokenLetters:
                if key in word:
                    words -= 1
                    break
            words += 1
        return words

        # # Optimized approach:
        # # Convert brokenLetters into a set for O(1) lookup
        # broken_set = set(brokenLetters)

        # # Use a generator expression to count words that are fully typable
        # return sum(1 for word in text.split() if not any(char in broken_set for char in word))
