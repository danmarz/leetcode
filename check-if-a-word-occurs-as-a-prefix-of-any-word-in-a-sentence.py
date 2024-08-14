class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # Split the sentence into a list of words
        words = sentence.split()

        # Iterate through the list of words with their index
        for i, word in enumerate(words):
            # Check if searchWord is a prefix of the current word
            if word.startswith(searchWord):
                # Return the index of the word (1-indexed, so add 1)
                return i + 1

        # If no word starts with searchWord, return -1
        return -1
