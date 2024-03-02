class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Create a set of banned words for efficient lookup
        banned_set = set(banned)

        # Create a dictionary to store the frequency count of each word
        word_count = {}

        # Split the paragraph into words using regular expressions
        words = re.findall(r"\w+", paragraph.lower())

        # Iterate through each word
        for word in words:
            # Skip the word if it is in the set of banned words
            if word not in banned_set:
                word_count[word] = word_count.get(word, 0) + 1

        # Find the word with the maximum frequency count
        print(word_count)
        max_word = max(word_count, key=word_count.get)

        return max_word

        """
        lowercaseParagraph = paragraph.lower()
        delimiters = [",", "|", ";", "!",".","?","'"]

        for delimiter in delimiters:
            lowercaseParagraph = " ".join(lowercaseParagraph.split(delimiter))

        words = {}

        for word in lowercaseParagraph.split():
            if words.get(word):
                words[word] += 1
            else:
                words[word] = 1

        sortedWords = sorted(words.items(), key=lambda x:x[1], reverse=True)
        words = dict(sortedWords)

        for word in words:
            if word not in banned:
                return word
        """
