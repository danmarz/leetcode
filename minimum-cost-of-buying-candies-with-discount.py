class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # if len(cost) == 1:
        #     return cost[0]

        # cost = sorted(cost, reverse=True)
        # min_cost = 0

        # for i in range(0, len(cost), 3):
        #     candies = cost[i:i+3]
        #     print(candies)
        #     if len(candies) == 3:
        #         min_cost += candies[0] + candies[1]
        #     elif len(candies) == 2:
        #         min_cost += candies[0] + candies[1]
        #     else:
        #         min_cost += candies[0]

        # return min_cost

        # Smarter alternative:
        # Sort candies in descending order
        cost.sort(reverse=True)

        total_cost = 0
        n = len(cost)

        for i in range(n):
            # Only add the cost of the first two candies in every triplet
            if i % 3 != 2:  # Skip every third candy
                total_cost += cost[i]

        return total_cost
