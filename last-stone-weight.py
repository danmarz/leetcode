class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert stones to negative values to simulate a max-heap
        stones = [-stone for stone in stones]
        heapq.heapify(stones)  # Convert the list to a heap

        # Perform smashing until there is at most one stone left
        while len(stones) > 1:
            # Get the two heaviest stones
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            # If x != y, push the remaining stone back into the heap
            if x != y:
                heapq.heappush(stones, x - y)

        # Return the weight of the last remaining stone (if any)
        return -stones[0] if stones else 0
