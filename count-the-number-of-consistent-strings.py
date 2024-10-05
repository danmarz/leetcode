class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent = 0
        allowedSet = set(allowed)

        for word in words:
            # if set(word).issubset(allowedSet):
            #     consistent += 1

            # Alternative approach: loop through each character in the word and check if it is in the allowedSet.
            # This way, the algorithm can exit early if a non-allowed character is found, potentially
            # improving performance.

            if all(
                char in allowedSet for char in word
            ):  # Check all characters in the word
                consistent += 1
        return consistent
