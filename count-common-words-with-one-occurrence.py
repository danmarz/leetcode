class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words_count1 = {}
        words_count2 = {}

        for word in words1:
            if word not in words_count1:
                words_count1[word] = 1
            else:
                words_count1[word] += 1

        for word in words2:
            if word not in words_count2:
                words_count2[word] = 1
            else:
                words_count2[word] += 1

        common_words = set(
            word for word in words_count1.keys() if words_count1[word] == 1
        ) & set(word for word in words_count2.keys() if words_count2[word] == 1)

        return len(common_words)

        # # More pythonic approach:
        # # Count occurrences of each word in both lists
        # count1 = Counter(words1)
        # count2 = Counter(words2)

        # # Find words that appear exactly once in both arrays
        # common_words = {word for word in count1 if count1[word] == 1 and count2.get(word, 0) == 1}

        # return len(common_words)
