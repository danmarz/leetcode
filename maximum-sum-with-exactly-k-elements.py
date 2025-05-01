class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        # Convert nums to a max-heap by pushing negative values (heapq is min-heap by default)
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        score = 0

        for _ in range(k):
            # Pop the largest element (remember to negate it back)
            m = -heapq.heappop(max_heap)

            # Add its value to the score
            score += m

            # Push m + 1 back into the heap (negated again)
            heapq.heappush(max_heap, -(m + 1))

        return score
