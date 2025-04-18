class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children  # Everyone gets at least $1
        if money < 0:
            return -1

        eight = min(money // 7, children)  # Try giving $7 more to some kids (total $8)
        money -= eight * 7
        children -= eight

        # Special checks to avoid anyone ending up with exactly $4 or leftover money
        if (children == 0 and money > 0) or (children == 1 and money == 3):
            eight -= 1

        return max(eight, 0)
