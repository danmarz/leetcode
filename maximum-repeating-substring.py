class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        concatenated_word = word

        # Keep checking until the concatenated word is no longer a substring of the sequence
        while concatenated_word in sequence:
            k += 1
            concatenated_word += word  # Add another repetition of 'word'

        return k
