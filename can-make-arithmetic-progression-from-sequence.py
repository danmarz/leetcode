class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # Sort the array
        arr.sort()

        # Calculate the difference between the first two elements
        diff = arr[1] - arr[0]

        # Check the difference between all consecutive elements
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False

        # If all differences are the same, return True
        return True
