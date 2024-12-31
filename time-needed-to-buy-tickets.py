class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # count = 0

        # while tickets[k] > 0:
        #     for i in range(len(tickets)):
        #         if tickets[i] > 0:
        #             tickets[i] -= 1
        #             count += 1

        #         if tickets[k] == 0:
        #             break

        # return count

        # Optimized O(n) solution
        total_time = 0
        for i in range(len(tickets)):
            if i <= k:
                total_time += min(tickets[i], tickets[k])
            else:
                total_time += min(tickets[i], tickets[k] - 1)
        return total_time
