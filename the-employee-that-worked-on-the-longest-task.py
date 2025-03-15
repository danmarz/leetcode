class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        longest = -1
        employee_id = -1
        last_start_time = 0

        for id, time in logs:
            if (time - last_start_time) == longest:
                employee_id = min(employee_id, id)
            elif (time - last_start_time) > longest:
                longest = time - last_start_time
                employee_id = id
            last_start_time = time

        return employee_id
