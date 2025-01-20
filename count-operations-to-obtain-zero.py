class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # if num1 == 0 or num2 == 0:
        #     return 0
        # count = 1

        # while abs(num1 - num2) != 0:
        #     if num1 >= num2:
        #         num1 -= num2
        #     else:
        #         num2 -= num1
        #     count += 1

        # return count

        return (
            0
            if num1 * num2 == 0
            else num1 // num2 + self.countOperations(num2, num1 % num2)
        )
