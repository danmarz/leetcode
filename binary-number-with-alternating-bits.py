class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Convert the integer to binary representation
        binary_str = bin(n)[2:]

        # Check if there are no consecutive equal bits in the binary string
        return "00" not in binary_str and "11" not in binary_str

        # Looping alternative
        """
        num_str = str(bin(n))[2:]
        previous = -99
        
        for pos, char in enumerate(num_str):
            if char == previous:
                return False
            previous = char
        return True
        """
