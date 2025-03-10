class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        def date_to_days(date: str) -> int:
            """Converts a MM-DD date string to the number of days since the start of the year."""
            month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            month, day = map(int, date.split("-"))
            return sum(month_days[: month - 1]) + day

        start = max(date_to_days(arriveAlice), date_to_days(arriveBob))
        end = min(date_to_days(leaveAlice), date_to_days(leaveBob))

        return max(0, end - start + 1)
