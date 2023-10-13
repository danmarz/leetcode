class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []

        for i in range(n + 1):
            arr.append(int(str(bin(i)).count("1")))

        return arr
