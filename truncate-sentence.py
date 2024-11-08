class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # s_arr = s.split(' ')
        # return " ".join(s_arr[:k])

        # Optimized approach for better memory handling
        count = 0
        index = -1
        for i, char in enumerate(s):
            if char == " ":
                count += 1
                if count == k:
                    index = i
                    break
        return s[:index] if index != -1 else s
