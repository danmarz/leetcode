class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # Convert the number to a string to easily access each digit
        digits = [int(d) for d in str(n)]

        # Compute the product of the digits
        product = 1
        for digit in digits:
            product *= digit

        # Compute the sum of the digits
        digit_sum = sum(digits)

        # Compute the difference between the product and the sum
        result = product - digit_sum

        return result
