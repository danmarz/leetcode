import time


class Solution:
    def average(self, salary: List[int]) -> float:
        # averageS = sorted(salary)
        # averageS = averageS[1:-1]
        # return sum(averageS) / len(averageS)

        # Proof that arr.sort() is faster than sorted(arr)
        arr = list(range(1000000, 0, -1))

        # Timing arr.sort()
        start_time = time.time()
        arr.sort()
        print("arr.sort() took", time.time() - start_time, "seconds")

        # Resetting arr for the next test
        arr = list(range(1000000, 0, -1))

        # Timing sorted(arr)
        start_time = time.time()
        sorted_arr = sorted(arr)
        print("sorted(arr) took", time.time() - start_time, "seconds")

        # Therefore this solution results more efficient than using sorted():
        salary.sort()  # O(n log n)
        return sum(salary[1:-1]) / (len(salary) - 2)  # O(n)

        # Alternative without performing any sorting op

        # # Initialize min and max with extreme values
        # min_salary = float('inf')
        # max_salary = float('-inf')
        # total_sum = 0

        # # Loop through the salary list to find min, max, and total sum
        # for s in salary:
        #     # Update min_salary and max_salary
        #     if s < min_salary:
        #         min_salary = s
        #     if s > max_salary:
        #         max_salary = s
        #     # Add the salary to total_sum
        #     total_sum += s

        # # Subtract min and max from total sum and calculate average
        # return (total_sum - min_salary - max_salary) / (len(salary) - 2)
