class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # Initialize the total number of bottles you can drink with the initially full bottles
        total_drunk = numBottles

        # While you have enough empty bottles to exchange for at least one full bottle
        while numBottles >= numExchange:
            # Calculate the number of new bottles you can get by exchanging empty bottles
            new_bottles = numBottles // numExchange

            # Calculate the remaining empty bottles after the exchange
            numBottles = new_bottles + (numBottles % numExchange)

            # Add the new full bottles to the total number of bottles you can drink
            total_drunk += new_bottles

        # Return the total number of bottles you were able to drink
        return total_drunk

        # Alternative approach:

        # # Initialize the number of bottles drunk as the initially full bottles
        # drunkBottles = numBottles

        # # Initialize the number of empty bottles to the initial number of bottles
        # emptyBottles = numBottles

        # # Loop as long as there are enough empty bottles to exchange for at least one full bottle
        # while emptyBottles >= numExchange:
        #     # Exchange empty bottles for one full bottle
        #     emptyBottles -= numExchange

        #     # Increment the count of drunk bottles as you get a new full bottle
        #     drunkBottles += 1

        #     # After drinking the new bottle, you get an additional empty bottle
        #     emptyBottles += 1

        # # Return the total number of bottles drunk
        # return drunkBottles
