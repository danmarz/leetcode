class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Length of the string
        n = len(s)

        # Check substrings of different lengths for repeated patterns
        for length in range(1, n // 2 + 1):
            if n % length == 0:
                num_repeats = n // length
                substring = s[:length]
                constructed_string = substring * num_repeats

                # If the constructed string matches the original string, return True
                if constructed_string == s:
                    return True

        return False
