class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0

        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i, 0)  # Insert duplicate zero at index i
                arr.pop()  # Remove an element from the end of the array to keep it the same
                i += 2  # Skip the inserted zeros
            else:
                i += 1
