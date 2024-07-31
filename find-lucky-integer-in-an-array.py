class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # Step 1: Count the frequency of each integer
        frequency = {}
        for num in arr:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        # Step 2: Identify lucky integers
        lucky_integers = [num for num in frequency if num == frequency[num]]

        # Step 3: Find the largest lucky integer
        if lucky_integers:
            return max(lucky_integers)
        else:
            return -1
