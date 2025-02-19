class Solution:
    def countAsterisks(self, s: str) -> int:
        group = False
        count = 0
        for c in s:
            if c == "|" and not group:
                group = True
            elif c == "|" and group:
                group = False
            elif c == "*" and not group:
                count += 1
        return count
