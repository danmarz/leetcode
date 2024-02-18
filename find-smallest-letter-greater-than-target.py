class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Initialize the result variable with the first character in letters
        result = letters[0]

        # Iterate through each character in letters
        for letter in letters:
            # If the current letter is greater than the target, update the result
            if letter > target:
                return letter

        # If no character is greater than the target, return the first character in letters
        return result
