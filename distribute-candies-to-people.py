class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        curr_candies = 1
        index = 0

        # Iterate through the candies to distribute
        while candies > 0:
            # Assign candies to the current person
            result[index] += min(candies, curr_candies)
            candies -= curr_candies
            curr_candies += 1
            index = (index + 1) % num_people

        return result
