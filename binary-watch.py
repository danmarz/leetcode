class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def countBits(num):
            # Count the number of 1s in the binary representation of num.
            # Alternatively, return bin(num).count('1')
            count = 0
            while num:
                count += num & 1
                num >>= 1
            return count

        result = []

        for hour in range(12):
            for minute in range(60):
                if countBits(hour) + countBits(minute) == turnedOn:
                    # If the total number of turned-on LEDs matches turnedOn, add the time to the result.
                    result.append(f"{hour}:{minute:02}")

        return result
