class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        # count1 = Counter(word1)
        # count2 = Counter(word2)

        # for key in count1:
        #     diff = abs(count1[key] - count2[key])
        #     if diff > 3:
        #         return False

        # for key in count2:
        #     diff = abs(count1[key] - count2[key])
        #     if diff > 3:
        #         return False

        # return True

        ### Alternative, optimized solution:
        count1 = Counter(word1)
        count2 = Counter(word2)

        # Combine keys from both counters
        all_keys = set(count1.keys()).union(count2.keys())

        # Check frequency differences
        for key in all_keys:
            if abs(count1[key] - count2[key]) > 3:
                return False

        return True
