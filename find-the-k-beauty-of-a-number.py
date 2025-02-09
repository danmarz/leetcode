class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        str_num = str(num)
        count = 0

        for i in range(0, len(str_num) - k + 1):
            substring = int(str_num[i : i + k])
            if substring and num % substring == 0:
                count += 1

        return count
