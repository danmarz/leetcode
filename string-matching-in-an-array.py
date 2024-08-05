class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []

        for word in words:
            for i in words:
                if (
                    word in i and word is not i and word not in ans
                ):  # alternative, we can declare ans as a set and skip the last check for duplicates here (using add instead of append below)
                    ans.append(word)
        return ans
