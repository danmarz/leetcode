class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Initialize a dictionary to count the frequency of each character in s.
        char_count = {}
        
        # Count the frequency of characters in s.
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Iterate through t and check the character frequency.
        for char in t:
            if char not in char_count or char_count[char] == 0:
                return char
            char_count[char] -= 1

        # If no extra character is found in t, return an empty string or handle it as needed.
        return ""
        
        """ Bruteforce approach
        s_arr = sorted([i for i in s])
        t_arr = sorted([j for j in t])

        for i in range(len(s_arr)):
            if t_arr[i] != s_arr[i]:
                return t_arr[i]
        
        return t_arr[-1]
        ""