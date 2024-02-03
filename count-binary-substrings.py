class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Initialize variables
        prev_count, curr_count, result = 0, 1, 0

        # Iterate through the string starting from the second character
        for i in range(1, len(s)):
            # If the current character is equal to the previous one, increment current count
            if s[i] == s[i - 1]:
                curr_count += 1
            else:
                # If the current character is different, update previous count and reset current count
                prev_count = curr_count
                curr_count = 1

            # If the current count is less than or equal to the previous count, add it to the result
            if curr_count <= prev_count:
                result += 1

        return result
