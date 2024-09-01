class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # Initialize a variable to count the number of good triplets
        good_triplets_count = 0

        # Get the length of the array
        n = len(arr)

        # Iterate over all possible triplets (i, j, k) with i < j < k
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):

                    # Check the first condition |arr[i] - arr[j]| <= a
                    if abs(arr[i] - arr[j]) <= a:

                        # Check the second condition |arr[j] - arr[k]| <= b
                        if abs(arr[j] - arr[k]) <= b:

                            # Check the third condition |arr[i] - arr[k]| <= c
                            if abs(arr[i] - arr[k]) <= c:

                                # If all conditions are satisfied, it's a good triplet
                                good_triplets_count += 1

        # Return the total count of good triplets
        return good_triplets_count
