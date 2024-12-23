class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        tokens = s.split()
        num = 0

        for token in tokens:
            if token.isdigit() and not token.startswith("0"):
                if int(token) > num:
                    num = int(token)
                else:
                    return False
        return True
