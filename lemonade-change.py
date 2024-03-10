class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Count of $5 and $10 bills currently available
        count_5 = count_10 = 0

        for bill in bills:
            if bill == 5:
                # Receive $5 bill, no change needed
                count_5 += 1
            elif bill == 10:
                # Receive $10 bill, need to give $5 change
                if count_5 == 0:
                    return False  # Cannot give change
                count_5 -= 1
                count_10 += 1
            elif bill == 20:
                # Receive $20 bill, need to give either (1) one $10 and one $5 or (2) three $5 bills
                if count_10 >= 1 and count_5 >= 1:
                    # Give one $10 and one $5 as change
                    count_10 -= 1
                    count_5 -= 1
                elif count_5 >= 3:
                    # Give three $5 bills as change
                    count_5 -= 3
                else:
                    return False  # Cannot give change

        return True  # Able to give change to all customers
