class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = {}
        pairs = 0

        for domino in dominoes:
            # Sort the domino pair in ascending order
            domino.sort()

            # Convert the sorted domino pair to a tuple for hashing
            domino_tuple = tuple(domino)

            # Increment the count for the current domino pair
            count[domino_tuple] = count.get(domino_tuple, 0) + 1

        # Count the number of pairs
        for val in count.values():
            pairs += (val * (val - 1)) // 2

        return pairs
