class Solution:
    def makeFancyString(self, s: str) -> str:
        # chars = {}
        # string = []
        # for pos, char in enumerate(s):
        #     string.append(char)
        #     if char not in chars:
        #         chars[char] = 1
        #     else:
        #         chars[char] += 1
        #         if chars[char] > 2 and (s[pos - 1] == char and s[pos - 2] == char):
        #             string.pop()
        # return "".join(string)

        # # Optimized approach: O(n)
        # Handle edge case for short strings
        if len(s) < 3:
            return s

        # Initialize a pointer for the result
        result = []  # Result will store the valid characters

        for char in s:
            # Append the character if it doesn't create three consecutive characters
            if len(result) < 2 or result[-1] != char or result[-2] != char:
                result.append(char)

        return "".join(result)
