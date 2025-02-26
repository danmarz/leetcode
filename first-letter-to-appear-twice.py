class Solution:
    def repeatedCharacter(self, s: str) -> str:
        c_set = set()

        for c in s:
            if not c in c_set:
                c_set.add(c)
            else:
                return c
