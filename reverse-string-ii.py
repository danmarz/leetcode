class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Convert the string to a list since strings are immutable in Python
        s_list = list(s)

        for i in range(0, len(s), 2 * k):
            # Reverse the first k characters in the segment
            s_list[i:i + k] = reversed(s_list[i:i + k])

        return ''.join(s_list)
