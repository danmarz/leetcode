class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # Get the length of the string
        n = len(s)
        # Initialize an empty list to store the result permutation
        result = []
        # Initialize two pointers to keep track of the next smallest and largest unused integers
        low, high = 0, n

        # Iterate through the string s
        for char in s:
            # If the current character is 'I', append the value of low to the result permutation
            # and increment low
            if char == "I":
                result.append(low)
                low += 1
            # If the current character is 'D', append the value of high to the result permutation
            # and decrement high
            else:
                result.append(high)
                high -= 1

        # Append the remaining value of low or high to the result permutation
        result.append(low)
        # Return the result permutation
        return result
