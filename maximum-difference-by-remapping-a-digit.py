class Solution:
    def minMaxDifference(self, num: int) -> int:
        # Convert number to string for digit manipulation
        s = str(num)

        # Get maximum value by replacing each unique digit with '9' one at a time
        max_val = num
        for d in set(s):
            if d != "9":
                # Replace all occurrences of d with '9'
                replaced = s.replace(d, "9")
                max_val = max(max_val, int(replaced))

        # Get minimum value by replacing each unique digit with '0' through '9'
        min_val = num
        for d in set(s):
            for replacement in "0123456789":
                if replacement == d:
                    continue
                # Replace all occurrences of d with the new digit
                replaced = s.replace(d, replacement)
                # Convert to int to ignore leading zeros
                min_val = min(min_val, int(replaced))

        # Return the difference
        return max_val - min_val
