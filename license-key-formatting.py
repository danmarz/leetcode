class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace(
            "-", ""
        ).upper()  # Remove dashes and convert characters to uppercase
        n = len(s)

        first_group_len = (
            n % k if n % k != 0 else k
        )  # Calculate the length of the first group

        reformatted_key = []
        count = 0

        # Construct the reformatted license key in reverse order
        for char in reversed(s):
            if count == k:
                reformatted_key.append("-")
                count = 0
            reformatted_key.append(char)
            count += 1

        return "".join(
            reformatted_key[::-1]
        )  # Reverse the constructed key to get the correct order
