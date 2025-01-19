class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # result = set()

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if i != j and (j, i) not in result and nums[i] == nums[j] and (i * j) % k == 0:
        #             result.add((i, j))

        # return len(result)

        # Optimized code:
        # Step 1: Group indices by the value of nums[i]
        index_map = defaultdict(list)
        for i, num in enumerate(nums):
            index_map[num].append(i)

        count = 0

        # Step 2: Iterate over groups to find valid pairs
        for indices in index_map.values():
            n = len(indices)
            for i in range(n):
                for j in range(i + 1, n):
                    # Check if the product of indices is divisible by k
                    if (indices[i] * indices[j]) % k == 0:
                        count += 1

        return count
