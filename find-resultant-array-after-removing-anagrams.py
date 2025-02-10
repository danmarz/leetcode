class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # sorted_words = ["".join(sorted(words[0]))]
        # result = [words[0]]
        # for i in range(1, len(words)):
        #     word = "".join(sorted(words[i]))
        #     if word not in sorted_words or sorted_words[-1] != word:
        #         result.append(words[i])
        #         sorted_words.append(word)
        # return result

        # Readwise, a more optimal apprach:
        def are_anagrams(word1: str, word2: str) -> bool:
            # Check if two words are anagrams by comparing their sorted characters
            return sorted(word1) == sorted(word2)

        result = [words[0]]  # Always keep the first word

        for i in range(1, len(words)):
            # Compare current word with the last word in the result list
            if not are_anagrams(words[i], result[-1]):
                result.append(words[i])

        return result
