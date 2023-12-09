class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # A more concise approach:
        # Check if all letters are uppercase or lowercase
        if word.isupper() or word.islower():
            return True

        # Check if only the first letter is uppercase
        if word[0].isupper() and word[1:].islower():
            return True

        return False

        """
        if word.islower():
            return True
        elif word.isupper():
            return True
        else:
            for pos,char in enumerate(word):
                if char.isupper() and word[pos + 1:].islower():
                    return True
                else:
                    return False
        """
