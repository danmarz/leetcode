class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:  # Iterate until the second-to-last element
            if bits[i] == 0:
                i += 1  # Move one position forward for one-bit character
            else:
                i += 2  # Move two positions forward for two-bit character
        return i == len(bits) - 1  # Check if the last character is a one-bit character
