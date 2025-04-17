class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:

        # Set for faster lookup
        vowels = {"a", "e", "i", "o", "u"}
        count = 0

        # Iterate directly over the range
        for i in range(left, right + 1):
            # Check if both first and last character are vowels
            if words[i][0] in vowels and words[i][-1] in vowels:
                count += 1

        return count
