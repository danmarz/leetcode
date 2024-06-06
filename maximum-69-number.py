class Solution:
    def maximum69Number(self, num: int) -> int:
        # Convert the number to a string for easy manipulation
        num_str = str(num)

        # Traverse the string to find the first '6'
        for i in range(len(num_str)):
            if num_str[i] == "6":
                # Change the first '6' to '9'
                num_str = num_str[:i] + "9" + num_str[i + 1 :]
                break

        # Convert the modified string back to an integer and return
        return int(num_str)
