class Solution:
    def splitNum(self, num: int) -> int:
        n_lst = [n for n in sorted(str(num))]
        num1, num2 = "", ""

        for i in range(len(n_lst)):
            if i % 2 == 0:
                num1 += n_lst[i]
            else:
                num2 += n_lst[i]

        return int(num1) + int(num2)
