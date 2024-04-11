class Solution:
    def largestSumAfterKNegations(self, nums: List[int], K: int) -> int:
        heapify(min_heap)

        while K > 0:
            heappush(min_heap, -(heappop(min_heap)))
            K -= 1

        return sum(min_heap)
