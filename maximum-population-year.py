class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # Initialize the dictionary to store population changes
        changes = {}

        # Populate the dictionary with birth (+1) and death (-1) events
        for birth, death in logs:
            changes[birth] = changes.get(birth, 0) + 1
            changes[death] = changes.get(death, 0) - 1

        # print(changes)

        # Initialize variables for tracking
        max_population = 0
        current_population = 0
        earliest_year = None

        # Traverse years in sorted order, applying cumulative changes
        for year in sorted(changes.keys()):
            current_population += changes[year]

            # print(year, current_population)

            # Check if we found a new max population
            if current_population > max_population:
                max_population = current_population
                earliest_year = year

        # Return the earliest year with max population
        return earliest_year
