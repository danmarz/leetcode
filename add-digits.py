class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            # Convert the number to a string to iterate through its digits.
            num_str = str(num)
            # Sum the digits by converting them back to integers.
            num = sum(int(digit) for digit in num_str)
        return num
