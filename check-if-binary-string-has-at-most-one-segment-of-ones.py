class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # This is the better approach, given the string always starts with one 1 segment :)
        return "01" not in s

        # Bruteforce way: check each char position and compare it with the previous char
        # String always starts with a '1' in position 0, we check from pos 1
        # index = 1
        # one_segments = 0
        # while index < len(s):
        #     # Detect end of 1 seq.
        #     if s[index] == "0" and s[index - 1] == "1":
        #         one_segments += 1
        #         index += 1
        #     # Detect start of 1 seq.
        #     elif s[index] == "1" and s[index - 1] == "0":
        #         one_segments += 1
        #         index += 1
        #     # Move forward if there's no change
        #     else:
        #         index += 1
        #     if one_segments > 1:
        #         return False
        # return True
