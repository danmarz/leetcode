class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Optimized solution O(1)
        return (high + 1) // 2 - (low // 2)

    # # Adjust the range to start with the first odd number
    # if low % 2 == 0:
    #     low += 1

    # # Adjust the range to end with the last odd number
    # if high % 2 == 0:
    #     high -= 1

    # # If the adjusted low is greater than the adjusted high, there are no odd numbers
    # if low > high:
    #     return 0

    # # Calculate the number of odd numbers
    # return (high - low) // 2 + 1
