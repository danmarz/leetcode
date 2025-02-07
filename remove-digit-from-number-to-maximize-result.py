class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_number = ""

        # Iterate over the string and remove each occurrence of the digit
        for i in range(len(number)):
            if number[i] == digit:
                new_number = number[:i] + number[i + 1 :]  # Remove the digit at index i

                # Update max_number if the new_number is greater
                if not max_number or int(new_number) > int(max_number):
                    max_number = new_number

        return max_number
