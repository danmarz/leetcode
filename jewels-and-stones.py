class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
       # Convert jewels string to a set for faster lookup
        jewel_set = set(jewels)
        # Initialize a counter for the number of jewels found
        num_jewels = 0
        # Iterate through each stone in the stones string
        for stone in stones:
            # If the stone is a jewel, increment the counter
            if stone in jewel_set:
                num_jewels += 1
        # Return the total number of jewels found
        return num_jewels 