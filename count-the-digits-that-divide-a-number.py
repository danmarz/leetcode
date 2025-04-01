class Solution:
    def countDigits(self, num: int) -> int:
        str_num = str(num)
        count = 0
        for i in range(len(str_num)):
            if num % int(str_num[i]) == 0:
                count += 1
        return count
