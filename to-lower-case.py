class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""
        for char in s:
            # Check if the character is uppercase
            if "A" <= char <= "Z":
                # Convert the uppercase character to lowercase using ASCII values
                lowercase_char = chr(ord(char) + 32)
                result += lowercase_char
            else:
                # Append the character as it is if it's not uppercase
                result += char
        return result

        # Alternative solution (10ms faster)
        """
        ans = ""

        for char in s:
            if ord(char) < 91 and ord(char) > 64:
                char = chr(ord(char) + 32)
            ans += char
        
        return ans
        """
