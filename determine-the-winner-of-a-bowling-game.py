class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def calculate_score(throws):
            n = len(throws)
            score = 0

            for i in range(n):
                # Check if either of the two previous turns was a strike (10 pins)
                if (i >= 1 and throws[i - 1] == 10) or (i >= 2 and throws[i - 2] == 10):
                    score += 2 * throws[i]  # Double the value
                else:
                    score += throws[i]  # Regular value
            return score

        score1 = calculate_score(player1)
        score2 = calculate_score(player2)

        if score1 > score2:
            return 1
        elif score2 > score1:
            return 2
        else:
            return 0

        # n = len(player1)
        # if n == 1:
        #     if player1[0] == player2[0]:
        #         return 0
        #     else:
        #         return 1 if player1[0] > player2[0] else 2

        # prev1 = player1[0]
        # prevPrev1 = player1[1]
        # if prev1 == 10:
        #     score1 = player1[0] + 2 * player1[1]
        # else:
        #     score1 = player1[0] + player1[1]
        # prev2 = player2[0]
        # if prev2 == 10:
        #     prevPrev2 = 2 * player2[1]
        # else:
        #     prevPrev2 = player2[1]
        # if prev2 == 10:
        #     score2 = player2[0] + 2 * player2[1]
        # else:
        #     score2 = player2[0] + player2[1]
        # for i in range(2, len(player1)):
        #     if prev1 == 10 or prevPrev1 == 10:
        #         score1 += (2 * player1[i])
        #     else:
        #         score1 += player1[i]
        #     prev1 = player1[i]
        #     prevPrev1 = player1[i - 1]
        #     if prev2 == 10 or prevPrev2 == 10:
        #         score2 += (2 * player2[i])
        #     else:
        #         score2 += player2[i]
        #     prev2 = player2[i]
        #     prevPrev2 = player2[i - 1]
        #     print(score1, score2)

        # if score1 == score2:
        #     return 0
        # elif score1 > score2:
        #     return 1
        # else:
        #     return 2
