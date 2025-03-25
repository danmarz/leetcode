class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()

        if sentence[0] != sentence[-1]:
            return False
        for i in range(len(words) - 1):
            if words[i + 1][0] != words[i][-1]:
                return False
        return True
