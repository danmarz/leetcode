class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        occurrences = []

        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                occurrences.append(words[i + 2])

        return occurrences

        """
        arr = text.split(" ")
        ans = []

        for pos, word in enumerate(arr):
            if pos < (len(arr) - 2) and word == first and arr[pos + 1] == second:
                ans.append(arr[pos + 2])

        return ans
        """
