class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # seconds = 0

        # while sum(amount) > 0:
        #     amount = sorted(amount, reverse=True)
        #     if amount[0] and amount[1]:
        #         amount[0] -= 1
        #         amount[1] -= 1
        #     else:
        #         amount[0] -= 1
        #     seconds += 1

        # return seconds

        # Optimized approach using mathematical reasoning:
        return max(max(amount), (sum(amount) + 1) // 2)
