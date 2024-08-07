class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        numbers = []

        # Separate letters and numbers
        for char in s:
            if char.isalpha():
                letters.append(char)
            else:
                numbers.append(char)

        # Check if it's possible to interleave letters and numbers
        if abs(len(letters) - len(numbers)) > 1:
            return ""

        # Ensure letters start if they are more or equal to numbers
        if len(letters) < len(numbers):
            letters, numbers = numbers, letters

        # Interleave letters and numbers
        ans = []
        for i in range(len(s)):
            if i % 2 == 0:
                ans.append(letters.pop())
            else:
                ans.append(numbers.pop())

        return "".join(ans)


## Alternative approach
class Solution:
    def reformat(self, s: str) -> str:
        letters = [char for char in s if char.isalpha()]
        numbers = [char for char in s if char.isdigit()]

        if abs(len(letters) - len(numbers)) > 1:
            return ""

        if len(letters) < len(numbers):
            letters, numbers = numbers, letters

        result = [None] * len(s)
        result[::2] = letters
        result[1::2] = numbers

        return "".join(result)
