class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split the sentences into lists of words
        words1 = s1.split()
        words2 = s2.split()

        # Dictionary to store word counts
        word_counts = {}

        # Update word counts for sentence 1
        for word in words1:
            word_counts[word] = word_counts.get(word, 0) + 1

        # Update word counts for sentence 2
        for word in words2:
            word_counts[word] = word_counts.get(word, 0) + 1

        # Filter uncommon words
        uncommon_words = [word for word, count in word_counts.items() if count == 1]

        return uncommon_words
