class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize the frequency dictionary with the characters in the first word
        freq_dict = {}
        for char in words[0]:
            freq_dict[char] = freq_dict.get(char, 0) + 1

        # Iterate through the remaining words and update the frequency dictionary
        for word in words[1:]:
            word_freq = {}
            for char in word:
                if char in freq_dict:
                    word_freq[char] = word_freq.get(char, 0) + 1

            # Update the frequency dictionary to only include characters common between the current word and the dictionary
            for char, freq in freq_dict.items():
                if char in word_freq:
                    freq_dict[char] = min(freq, word_freq[char])
                else:
                    freq_dict[char] = 0

        # Construct a list of characters that appear in all words based on the frequency dictionary
        result = []
        for char, freq in freq_dict.items():
            result.extend([char] * freq)

        return result
