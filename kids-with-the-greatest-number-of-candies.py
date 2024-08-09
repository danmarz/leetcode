class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Step 1: Find the current maximum number of candies any kid has
        max_candies = max(candies)

        # Step 2: Initialize an empty result list to store the boolean results
        result = []

        # Step 3: Iterate through each kid's candies
        for candy in candies:
            # Step 4: Calculate the potential candies if this kid gets all the extra candies
            potential_candies = candy + extraCandies

            # Step 5: Compare the potential candies with the maximum candies
            if potential_candies >= max_candies:
                # If the potential candies is greater than or equal to the maximum, append True
                result.append(True)
            else:
                # Otherwise, append False
                result.append(False)

        # Step 6: Return the result list
        return result
