class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # Initialize the result array with the first element already known
        decoded = [first]

        # Loop through the encoded array and calculate the original array
        for i in range(len(encoded)):
            # decoded[i + 1] = encoded[i] XOR decoded[i]
            # Append the next element to decoded by XORing encoded[i] with the last element of decoded
            decoded.append(decoded[i] ^ encoded[i])

        # Return the decoded original array
        return decoded
