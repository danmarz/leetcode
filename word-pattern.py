class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        ## The conditions for bijectivity are satisfied if and only if the following is true:
        ## The counts of distinct elements in two groups + the count of distinct mappings are all equal.

        return (
            len(set(pattern))  # 1st group
            == len(set(s))  # 2nd group
            == len(set(zip_longest(pattern, s)))  # Distinct mappings
        )

        """
        words = s.split()
        
        # Check if the lengths of pattern and words are different.
        if len(pattern) != len(words):
            return False

        char_to_word = {}  # Dictionary to store the mapping from pattern to word.
        word_to_char = {}  # Dictionary to store the mapping from word to pattern.

        for char, word in zip(pattern, words):
            if char in char_to_word:
                # If the character in pattern is already mapped to a different word, return False.
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word

            if word in word_to_char:
                # If the word is already mapped to a different character in pattern, return False.
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char

        # If we haven't returned False by this point, the bijection exists.
        return True
        """
