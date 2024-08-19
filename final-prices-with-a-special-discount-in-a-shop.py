class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Initialize the answer array with the same values as prices
        answer = prices[:]

        # Iterate over each item in the prices array
        for i in range(len(prices)):
            # Iterate over the subsequent items to find the discount
            for j in range(i + 1, len(prices)):
                # Check if the price at index j is less than or equal to the price at index i
                if prices[j] <= prices[i]:
                    # Apply the discount by subtracting prices[j] from prices[i]
                    answer[i] = prices[i] - prices[j]
                    # Once the discount is applied, break the loop
                    break

        # Return the final prices after applying discounts
        return answer
