class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_from_right = (
            -1
        )  # Initialize the max_from_right with -1 for the last element

        # Traverse the array from right to left
        for i in range(n - 1, -1, -1):
            # Store the current element before it gets replaced
            current = arr[i]
            # Replace the current element with the max_from_right
            arr[i] = max_from_right
            # Update max_from_right
            if current > max_from_right:
                max_from_right = current

        return arr
