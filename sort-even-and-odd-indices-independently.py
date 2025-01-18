class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # odd = []
        # even = []

        # for i in range(len(nums)):
        #     if i % 2 == 0:
        #         even.append(nums[i])
        #     else:
        #         odd.append(nums[i])

        # odd.sort(reverse=True)
        # even.sort()

        # ans = []

        # for i in range(len(nums)):
        #     if i % 2 == 0:
        #         ans.append(even.pop(0))
        #     else:
        #         ans.append(odd.pop(0))

        # return ans

        # Optimized solution, avoiding the shift-left cost of list.pop(0)
        # Separate even and odd indexed elements
        even_indices = [nums[i] for i in range(0, len(nums), 2)]
        odd_indices = [nums[i] for i in range(1, len(nums), 2)]

        # Sort even indices in non-decreasing order
        even_indices.sort()

        # Sort odd indices in non-increasing order
        odd_indices.sort(reverse=True)

        # Merge the sorted lists back into the original array
        result = []
        even_idx, odd_idx = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:  # Even index
                result.append(even_indices[even_idx])
                even_idx += 1
            else:  # Odd index
                result.append(odd_indices[odd_idx])
                odd_idx += 1

        return result
