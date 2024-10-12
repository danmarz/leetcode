class Solution:
    def totalMoney(self, n: int) -> int:
        # Optimal solution, time complexity O(1) due to simple arithmetic
        weeks = n // 7  # Number of full weeks
        days = n % 7  # Remaining days after full weeks

        # Sum for full weeks: using the formula for the sum of an arithmetic series
        # Each week contributes a sum: 7 * (week_start_value)
        total = 0
        for i in range(weeks):
            total += sum(range(1 + i, 8 + i))  # Summing values for each week
            print(total)

        # Sum for remaining days (partial week), starting from `weeks + 1`
        total += sum(range(weeks + 1, weeks + 1 + days))

        return total

        # # Easier to understand, but slower for large inputs -- O(n)
        # daily = 0
        # monday = 0
        # total = 0

        # for i in range(n):
        #     if i % 7 == 0:
        #         monday += 1
        #         total += monday
        #         daily = monday
        #     else:
        #         daily += 1
        #         total += daily

        # return total
