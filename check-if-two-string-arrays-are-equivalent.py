class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Concatenate the lists of strings and directly compare them
        return "".join(word1) == "".join(word2)
