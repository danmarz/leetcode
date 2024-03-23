class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # Convert the string to a list for easier manipulation
        s = list(s)

        # Initialize two pointers, one from the start and the other from the end
        left, right = 0, len(s) - 1

        # Iterate until the pointers meet
        while left < right:
            # Move the left pointer to the next alphabetic character
            while left < right and not s[left].isalpha():
                left += 1

            # Move the right pointer to the previous alphabetic character
            while left < right and not s[right].isalpha():
                right -= 1

            # Swap the alphabetic characters
            s[left], s[right] = s[right], s[left]

            # Move both pointers towards the center
            left += 1
            right -= 1

        # Convert the list back to a string and return
        return "".join(s)
