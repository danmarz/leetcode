class Solution:
    def similarPairs(self, words: List[str]) -> int:
        freq = defaultdict(int)

        for word in words:
            signature = tuple(sorted(set(word)))
            freq[signature] += 1

        pairs = 0
        for count in freq.values():
            if count > 1:
                pairs += count * (count - 1) // 2

        return pairs
