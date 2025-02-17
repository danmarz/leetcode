class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        prev = 0
        tax = 0

        for limit, percent in brackets:
            if income >= (limit - prev):
                tax += (limit - prev) * (percent / 100)
                income -= limit - prev
                prev = limit
            else:
                tax += income * (percent / 100)
                break

        return tax
