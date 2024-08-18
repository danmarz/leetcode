class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Create an empty list to hold the rearranged elements
        result = []

        # Iterate over the first half of the array (x1, x2, ..., xn)
        for i in range(n):
            # Append the current element from the first half (xi)
            result.append(nums[i])
            # Append the corresponding element from the second half (yi)
            result.append(nums[i + n])

        # Return the rearranged array
        return result
