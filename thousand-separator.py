class Solution:
    def thousandSeparator(self, n: int) -> str:
        # Pythonic way
        return f"{n:,}".replace(
            ",", "."
        )  # Format with commas and replace them with dots

        # # Bruteforce way
        # nString = str(n)   # Convert the integer to a string
        # thousands = []     # List to hold chunks of three digits
        # rest = ""          # Temporary string to collect digits for each chunk

        # # Loop through the string in reverse to group digits by thousands
        # for i in range(len(nString) - 1, -1, -1):
        #     rest = nString[i] + rest  # Prepend the current digit to maintain the correct order

        #     # Once the rest string reaches three characters, store it in the list
        #     if len(rest) == 3:
        #         thousands.append(rest)
        #         rest = ""  # Reset the rest string for the next chunk

        # # If any remaining digits are left (for numbers not divisible by 3), add them to the list
        # if rest:
        #     thousands.append(rest)

        # # Reverse the chunks and join them with dots (thousands separator)
        # return '.'.join(thousands[::-1])
