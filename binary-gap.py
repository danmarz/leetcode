class Solution:
    def binaryGap(self, n: int) -> int:
        # Convert the integer to its binary representation
        binary = bin(n)[2:]

        # Initialize variables to track the longest distance and the position of the last 1
        max_distance = 0
        prev = -1

        # Iterate through each bit in the binary representation
        for i, bit in enumerate(binary):
            # If the current bit is 1
            if bit == "1":
                # If this is not the first 1 encountered, calculate the distance
                if prev != -1:
                    distance = i - prev
                    max_distance = max(max_distance, distance)
                # Update the position of the last 1
                prev = i

        return max_distance
