class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # # the usual bruteforce implementation:
        # start_string = bin(start)[2:]
        # goal_string = bin(goal)[2:]

        # offset = abs(len(start_string) - len(goal_string))
        # flips = 0

        # if start > goal:
        #     for i in range(offset):
        #         if start_string[i] != '0':
        #             flips += 1
        #     for i in range(offset, len(start_string)):
        #         if start_string[i] != goal_string[i - offset]:
        #             flips += 1
        # else:
        #     for i in range(offset):
        #         if goal_string[i] != '0':
        #             flips += 1
        #     for i in range(offset, len(goal_string)):
        #         if goal_string[i] != start_string[i - offset]:
        #             flips += 1

        # return flips

        # XOR alternative:
        # XOR to find differing bits
        xor = start ^ goal

        # Count the number of 1s in the XOR result
        bit_flips = 0
        while xor > 0:
            bit_flips += xor & 1  # Check the last bit
            xor >>= 1  # Shift right to check the next bit

        return bit_flips

        # # Concise XOR alternative:
        # return bin(start ^ goal).count('1')
