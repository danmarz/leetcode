class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Initialize two variables to store the minimum cost to reach the first and second steps
        min_cost_1, min_cost_2 = cost[0], cost[1]

        # Iterate through the steps starting from the third step
        for i in range(2, len(cost)):
            # Calculate the minimum cost to reach the current step
            current_min_cost = cost[i] + min(min_cost_1, min_cost_2)

            # Update the minimum costs for the next iteration
            min_cost_1, min_cost_2 = min_cost_2, current_min_cost

        # Return the minimum cost to reach the top of the floor
        return min(min_cost_1, min_cost_2)
