class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)

        if n < 3:
            return False

        # Find the peak index
        peak_index = arr.index(max(arr))

        # Check if the peak is not at the start or end of the array
        if peak_index == 0 or peak_index == n - 1:
            return False

        # Check if the array is strictly increasing before the peak
        for i in range(peak_index):
            if arr[i] >= arr[i + 1]:
                return False

        # Check if the array is strictly decreasing after the peak
        for i in range(peak_index, n - 1):
            if arr[i] <= arr[i + 1]:
                return False

        return True
