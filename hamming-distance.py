class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR the two numbers to get the bit difference
        xor_result = x ^ y

        # Count the number of set bits in the XOR result
        distance = 0
        while xor_result:
            # Increment distance by 1 for each set bit (using bitwise AND operation)
            distance += xor_result & 1
            # Right shift the XOR result to check the next bit
            xor_result >>= 1

        return distance

        """
        # alternative (bruteforce)
        ans = 0

        # convert nums to binary strings
        stringX = str(bin(x))[2:]
        stringY = str(bin(y))[2:]

        # match string length by prepending 0
        if len(stringX) < len(stringY):
            for i in range(0,(len(stringY) - len(stringX))):
                stringX = "0" + stringX
        elif len(stringY) < len(stringX):
            for i in range(0,(len(stringX) - len(stringY))):
                stringY = "0" + stringY

        # check for different char(s)
        for i, val in enumerate(stringX):
            if val != stringY[i]:
                ans += 1

        return ans
        """
