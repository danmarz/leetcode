class Solution:
    def sortSentence(self, s: str) -> str:
        words_with_positions = s.split()
        reconstructed_sentence = [None] * len(words_with_positions)

        for word in words_with_positions:
            position = int(word[-1]) - 1  # Extract position (1-indexed to 0-indexed)
            reconstructed_sentence[position] = word[
                :-1
            ]  # Remove position and place in correct order

        return " ".join(reconstructed_sentence)
