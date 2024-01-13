class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Initialize a variable to count the number of new flowers that can be planted
        count = 0

        # Length of the flowerbed
        m = len(flowerbed)

        # Iterate through the flowerbed
        for i in range(m):
            # Check if the current plot is empty and its adjacent plots are also empty
            if (
                flowerbed[i] == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == m - 1 or flowerbed[i + 1] == 0)
            ):
                # Plant a flower in the current plot
                flowerbed[i] = 1
                # Increment the count of planted flowers
                count += 1

        # Check if the count of planted flowers is greater than or equal to the required number
        return count >= n
