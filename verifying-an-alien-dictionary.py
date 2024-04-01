class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def is_sorted(word1, word2, order):
            """
            Helper function to check if word1 comes before word2 lexicographically
            according to the given order.
            """
            for i in range(min(len(word1), len(word2))):
                if order[word1[i]] < order[word2[i]]:
                    return True
                elif order[word1[i]] > order[word2[i]]:
                    return False
            return len(word1) <= len(word2)

        # Create a dictionary to store the order of each letter in the alphabet
        order_dict = {char: i for i, char in enumerate(order)}

        # Iterate through each pair of adjacent words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            # Check if word1 comes after word2 lexicographically
            if not is_sorted(word1, word2, order_dict):
                return False

        # All pairs of adjacent words are sorted, so return True
        return True
