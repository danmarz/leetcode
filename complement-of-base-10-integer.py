class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # Step 1: Convert n to binary
        binary_n = bin(n)[2:]  # [2:] removes the '0b' prefix from the binary string

        # Step 2: Flip all the bits
        complement_bits = "".join(["1" if bit == "0" else "0" for bit in binary_n])

        # Step 3: Convert the binary representation back to an integer
        complement = int(complement_bits, 2)

        return complement
