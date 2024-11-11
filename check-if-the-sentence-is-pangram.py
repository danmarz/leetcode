class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Optimized solution using set comparison
        alphabet = set("abcdefghijklmnopqrstuvwxyz")
        sentence = set(sentence)
        return sentence >= alphabet

        # # Direct comparison, char in ...
        # alphabet = "abcdefghijklmnopqrstuvwxyz"
        # for char in alphabet:
        #     if char not in sentence:
        #         return False
        # return True
