class Solution:
    def trimMean(self, arr: List[int]) -> float:
        # Step 1: Sort the array
        arr.sort()

        # Step 2: Determine the number of elements to trim
        n = len(arr)
        trim_size = int(0.05 * n)  # 5% of total elements

        # Step 3: Slice the array to remove the smallest and largest 5%
        trimmed_arr = arr[trim_size : n - trim_size]

        # Step 4: Calculate and return the mean
        mean_value = sum(trimmed_arr) / len(trimmed_arr)

        return mean_value
