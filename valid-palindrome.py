class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters from string s
        s = "".join(c for c in s if c.isalnum())

        # Convert string sto lowercase
        s = s.lower()

        # Save the reversed string
        reversed_s = s[::-1]

        # Check if pali
        if len(s) == 0:
            return True
        for i in range(len(s) // 2):
            if s[i] != reversed_s[i]:
                return False
        return True
