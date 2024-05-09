from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Initialize a Counter for the characters in chars
        char_count = Counter(chars)
        # Initialize the total length of good strings
        total_length = 0
        
        # Iterate through each word in the list of words
        for word in words:
            # Initialize a Counter for the characters in the current word
            word_count = Counter(word)
            # Flag to indicate if the word can be formed using chars
            is_good = True
            
            # Check if each character in the word can be formed using chars
            for char, count in word_count.items():
                if char_count[char] < count:
                    is_good = False
                    break
            
            # If the word is good, add its length to the total length
            if is_good:
                total_length += len(word)
        
        return total_length
