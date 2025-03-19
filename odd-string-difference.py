class Solution:
    def oddString(self, words: List[str]) -> str:
        def get_diff_array(word):
                return tuple(ord(word[i+1]) - ord(word[i]) for i in range(len(word) - 1))

        diff_map = defaultdict(list)

        # Compute difference arrays for each word
        for word in words:
            diff_array = get_diff_array(word)
            diff_map[diff_array].append(word)

        # Find the unique difference array
        for diff_array, word_list in diff_map.items():
            if len(word_list) == 1:
                return word_list[0]

        return None  # Should never happen given valid input
