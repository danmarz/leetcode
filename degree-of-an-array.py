class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Dictionary to store the indices where each number appears
        num_indices = defaultdict(list)

        # Store the indices where each number appears
        for i, num in enumerate(nums):
            num_indices[num].append(i)

        # Find the maximum degree of the array
        max_degree = max(len(indices) for indices in num_indices.values())

        # Initialize the minimum length to positive infinity
        min_length = float("inf")

        # Iterate through the indices of each number
        for indices in num_indices.values():
            # If the number has the maximum degree, update the minimum length
            if len(indices) == max_degree:
                min_length = min(min_length, indices[-1] - indices[0] + 1)

        # Return the minimum length of the subarray
        return min_length
