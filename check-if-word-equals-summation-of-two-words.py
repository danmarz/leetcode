class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def getIntVal(word):
            s = ""
            for char in word:
                s += str(ord(char) - ord("a"))
            return int(s) if s else 0
            # # .join() approach is a more concise, performant, and pythonic(!) alternative of the code above
            # return int("".join(str(ord(char) - ord('a')) for char in word))

        num_firstWord = getIntVal(firstWord)
        num_secondWord = getIntVal(secondWord)
        num_targetWord = getIntVal(targetWord)

        return num_firstWord + num_secondWord == num_targetWord
