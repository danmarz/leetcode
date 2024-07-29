class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0

        for num1 in arr1:
            satisfies_condition = True

            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    satisfies_condition = False
                    break

            if satisfies_condition:
                count += 1

        return count
