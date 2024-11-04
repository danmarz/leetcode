class Solution:
    def secondHighest(self, s: str) -> int:
        # Initialize an empty set to store unique digits in the string
        seen = set()
        
        # Iterate through each character in the string
        for char in s:
            # Check if the character is a digit
            if char.isdigit():
                # Add the digit as an integer to the set
                seen.add(int(char))
        
        # Convert set to a sorted list (smallest to largest unique values)
        unique_sorted = sorted(seen)
        
        # If there are less than two unique numbers, return -1
        if len(unique_sorted) < 2:
            return -1
        
        # Return the second largest unique number
        return unique_sorted[-2]
        
        # nums = "0123456789"
        # seen = []
        # for char in s:
        #     if char in nums:
        #         seen.append(int(char))
        # seen.sort()
        # if len(set(seen)) < 2:
        #     return -1
        # max_num = seen[-1]
        # for i in reversed(range(len(seen))):
        #     if seen[i] < max_num:
        #         return seen[i]
