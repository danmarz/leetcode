class Solution:
    def greatestLetter(self, s: str) -> str:
        greatest = ""
        for char in s:
            if char.isupper() and char.lower() in s and char > greatest:
                greatest = char
        return greatest
