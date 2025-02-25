class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:  # Check for flush first
            return "Flush"

        rank_counts = Counter(ranks).values()

        if max(rank_counts) >= 3:
            return "Three of a Kind"
        elif max(rank_counts) == 2:
            return "Pair"

        return "High Card"
