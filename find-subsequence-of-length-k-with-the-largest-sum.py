class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # max_items = sorted(nums,reverse=True)[:k]
        # ans = []

        # for num in nums:
        #     if num in max_items:
        #         ans.append(num)
        #         max_items.remove(num)

        # return ans

        # Advanced solution, perserving the original indices while sorting:
        # Pair each number with its index
        indexed_nums = list(enumerate(nums))

        # Find the k largest elements (value-wise)
        largest_k = sorted(indexed_nums, key=lambda x: x[1], reverse=True)[:k]

        # Sort these elements by their original indices
        largest_k_sorted = sorted(largest_k, key=lambda x: x[0])

        # Extract the values from the sorted list
        return [x[1] for x in largest_k_sorted]
