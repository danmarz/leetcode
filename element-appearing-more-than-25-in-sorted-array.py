class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        n = len(arr)
        # Handle small arrays explicitly
        if n == 1 or n == 2 or n == 3:
            return arr[0]  # All elements are the same in this problem context

        threshold = n // 4

        # Check the elements at regular intervals
        for i in range(0, n, threshold):
            candidate = arr[i]

            # Check if the candidate occurs more than 25% of the time
            if arr.count(candidate) > threshold:
                return candidate

        # As per the problem description, there will always be such an element.
        # So the function should never reach this point.
        return -1

        """
        counter = Counter(arr)

        for el in counter.keys():
            if counter.get(el) > (len(arr) // 4):
                return el
        """
