class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # define vowels
        vowels = ["a", "e", "i", "o", "u"]

        # define the two halves vowels count
        a_vowels = 0
        b_vowels = 0

        # break s into a & b (in the same loop, for efficiency sake) and count vowels in each side
        for i in range(len(s) // 2):
            if s[i].lower() in vowels:
                a_vowels += 1
            if s[(len(s) // 2) + i].lower() in vowels:
                b_vowels += 1

        # return resulting equality
        return a_vowels == b_vowels

        # # Alternative solution, more efficient
        # # define ALL vowels (upper and lower case) as a set for efficient O(1) lookups
        # vowels = set('aeiouAEIOU')

        # # define the half-way point
        # n = len(s) // 2

        # # initialize the vowel balance count
        # count = 0

        # for i in range(n):
        #     # if left side is a vowel, increment the count
        #     if s[i] in vowels:
        #         count += 1
        #     # if right side is a vowel, decrement the count
        #     if s[i + n] in vowels:
        #         count -= 1

        # # return final count (if zero, both sides have an equal vowel count)
        # return count == 0

        # # Alternative solution, more concise
        # vowels = set('aeiouAEIOU')
        # n = len(s) // 2
        # return sum(c in vowels for c in s[:n]) == sum(c in vowels for c in s[n:])
