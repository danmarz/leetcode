class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # Not enough money to give each child at least $1
        if money < children:
            return -1

        # Try the maximum possible number of children with $8, down to 0
        for eights in range(min(children, money // 8), -1, -1):
            remaining_money = money - 8 * eights
            remaining_children = children - eights

            # Each remaining child needs at least $1
            if remaining_money < remaining_children:
                continue

            # Avoid the case where one child gets exactly $4
            if remaining_children == 1 and remaining_money == 4:
                continue

            # Valid distribution found
            return eights

        # If no valid distribution is possible
        return -1
