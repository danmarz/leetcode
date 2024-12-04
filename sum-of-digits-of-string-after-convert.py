class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Step 1: Convert string to numbers
        num_str = "".join(str(ord(char) - ord("a") + 1) for char in s)

        # Step 2: Transform into integer
        num = sum(int(digit) for digit in num_str)

        # Step 3: Perform the sum of digits k - 1 times (minus one transformation above)
        for _ in range(k - 1):
            num = sum(int(digit) for digit in str(num))

        return num

        # # Efficiently compute the initial sum directly
        # num = sum(int(digit) for char in s for digit in str(ord(char) - ord('a') + 1))

        # # Sum digits k times
        # for _ in range(k - 1):
        #     num = sum(int(digit) for digit in str(num))

        # return num
