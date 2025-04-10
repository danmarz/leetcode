class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Step 1: Convert gifts into a max heap by negating values
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)  # O(n)

        # Step 2: Perform k operations
        for _ in range(k):
            max_gift = -heapq.heappop(max_heap)  # Get the largest pile
            reduced_gift = int(max_gift**0.5)  # Floor of square root
            heapq.heappush(max_heap, -reduced_gift)  # Push it back into heap

        # Step 3: Sum the remaining gifts, negate values back to positive
        return -sum(max_heap)
