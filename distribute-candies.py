class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        max_candies = len(candyType) // 2
        unique_candies = len(set(candyType))

        return min(max_candies, unique_candies)
