class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # Calculate the total number of candies for Alice and Bob
        total_alice = sum(aliceSizes)
        total_bob = sum(bobSizes)

        # Create a set to store the sizes of candies that Alice has
        alice_set = set(aliceSizes)

        # Iterate through the candies that Bob has
        for b in bobSizes:
            # Calculate the size of the candy that Alice needs to exchange
            a = (total_alice - total_bob + 2 * b) / 2
            # If the size of the candy is present in the set, return the pair
            if a in alice_set:
                return [int(a), b]
