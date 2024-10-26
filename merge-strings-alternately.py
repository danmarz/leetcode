class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []  # Initialize an empty list for the merged characters
        min_len = min(len(word1), len(word2))  # Find the minimum length of both strings

        # Alternate characters from both words
        for i in range(min_len):
            merged.append(word1[i])
            merged.append(word2[i])

        # Append remaining characters from the longer word, if any
        if len(word1) > len(word2):
            merged.extend(word1[min_len:])
        else:
            merged.extend(word2[min_len:])

        return "".join(merged)  # Join the list into a single string

        # Slower (string manipulation) approach
        # i = 0
        # longe = word1 if len(word1) > len(word2) else word2
        # short = word1 if len(word1) < len(word2) else word2
        # merged_string = ""

        # while i < len(short):
        #     merged_string += word1[i] + word2[i]
        #     i += 1

        # while i < len(longe):
        #     merged_string += longe[i]
        #     i += 1

        # return merged_string
