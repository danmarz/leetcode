class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num = num / 2
                steps += 1
            else:
                num = num - 1
                steps += 1
        return steps

    """
    other solutions

    # 1.     
    
    Time:   O(log(n))
    Memory: O(log(n))

        def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + self.numberOfSteps(num - 1 if num & 1 else num >> 1)

    # 2.
    
    Time:   O(log(n))
    Memory: O(1)

        def numberOfSteps(self, num: int) -> int:
        steps = 0

        while num != 0:
            steps += 1
            if num & 1:
                num -= 1
            else:
                num >>= 1

        return steps
    
    # 3.

    Time:   O(1)
    Memory: O(1)

        def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        return num.bit_length() - 1 + num.bit_count()
"""
