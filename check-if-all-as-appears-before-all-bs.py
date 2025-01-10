class Solution:
    def checkString(self, s: str) -> bool:
        # seen_b = False

        # for c in s:
        #     if c == 'b' and not seen_b:
        #         seen_b = True
        #     if c == 'a' and seen_b:
        #         return False

        # return True

        # Optimized, short-circuit solution
        return "ba" not in s
