class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        joined_string = "".join(words)
        count = {}

        for i in joined_string:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        n = len(words)
        for char in count:
            if count[char] % n != 0:
                return False

        return True
