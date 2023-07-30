class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


# Other solutions
"""
    def isPalindrome(self, x: int) -> bool:
        a=list(str(x))
        b=list(str(x))
        b.reverse()
        return True if a==b else False
"""
"""
    def isPalindrome(self, x: int) -> bool:
        isPali = False
        text = str(x)
        check = 0

        for i in range(len(text)):
            if text[check] == text[len(text) - i - 1]:
                check += 1
                isPali = True
            else:
                return False
        return isPali
"""
