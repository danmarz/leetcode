class Solution:
    def mergeSimilarItems(
        self, items1: List[List[int]], items2: List[List[int]]
    ) -> List[List[int]]:
        items = defaultdict(int)

        for item_v, item_w in items1:
            items[item_v] += item_w

        for item_v, item_w in items2:
            items[item_v] += item_w

        return sorted(list(items.items()))
