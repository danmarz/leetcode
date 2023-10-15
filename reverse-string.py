class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        while left < right:
            # Swap the characters at the left and right pointers.
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        """ 
        # A valid and efficient approach: using slicing we create a reversed copy of the string and 
        # assigns it back to the original array, effectively reversing the characters in-place.

        s[:] = s[::-1]
        """

        """ Works but not modifying s in place
        reverse = []
        for char in reversed(s):
            reverse.append(char)
        s = reverse
        """
