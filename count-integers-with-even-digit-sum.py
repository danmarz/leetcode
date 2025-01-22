class Solution:
    def countEven(self, num: int) -> int:
        # result = []
        # for n in range(1, num + 1):
        #     n_string = str(n)
        #     digit_sum = sum(int(digit) for digit in n_string)
        #     if digit_sum % 2 == 0:
        #         result.append(n)

        # return len(result)

        # Optimized approach w/o using string conversion
        def digit_sum(n):
            """Calculate the sum of the digits of n."""
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total

        count = 0
        for i in range(1, num + 1):
            if digit_sum(i) % 2 == 0:  # Check if the digit sum is even
                count += 1

        return count
