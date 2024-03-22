class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # Count the frequency of each number in the deck
        freq = {}
        for num in deck:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Find the greatest common divisor of all frequencies
        gcd_val = None
        for count in freq.values():
            if gcd_val is None:
                gcd_val = count
            else:
                gcd_val = gcd(gcd_val, count)

        # Return true if the GCD is greater than 1, false otherwise
        return gcd_val > 1
