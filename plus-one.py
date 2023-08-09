class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def increaseDigit(d):
            return d + 1 if d < 9 else 0

        if digits[-1] == 9:
            s = [str(i) for i in digits]
            sum = int("".join(s)) + 1
            return map(int, str(sum))
        else:
            digits[-1] = increaseDigit(digits[-1])

        return digits

        # alternative solution: convert to string from start
        strings = ""
        for number in digits:
            strings += str(number)

        temp = str(int(strings) + 1)

        return [int(temp[i]) for i in range(len(temp))]

        # alternative solution: convert to string one liner
        return list(map(int, str(int("".join(map(str, digits))) + 1)))
