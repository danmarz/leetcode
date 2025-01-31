class Solution:
    def largestInteger(self, num: int) -> int:
        num_str = list(str(num))  # Convert number to list of digits
        odd_digits = sorted([d for d in num_str if int(d) % 2 == 1], reverse=True)
        even_digits = sorted([d for d in num_str if int(d) % 2 == 0], reverse=True)

        result = []

        for d in num_str:
            if int(d) % 2 == 1:
                result.append(odd_digits.pop(0))  # Replace with largest odd available
            else:
                result.append(even_digits.pop(0))  # Replace with largest even available

        return int("".join(result))  # Convert back to integer
