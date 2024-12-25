class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        moves = 0

        for i in range(len(seats)):
            # while seats[i] != students[i]:
            #     if seats[i] < students[i]:
            #         students[i] -= 1
            #         moves += 1
            #     else:
            #         students[i] += 1
            #         moves += 1

            # Optimized solution:
            moves += abs(seats[i] - students[i])

        return moves
