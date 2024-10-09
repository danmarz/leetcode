class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # from collections import Counter
        # Step 1: Count the number of students who prefer each type
        preference_count = Counter(students)

        # Step 2: Simulate the process of feeding students
        for sandwich in sandwiches:
            if preference_count[sandwich]:
                preference_count[sandwich] -= 1
            else:
                # No students prefer this sandwich; stop the process
                break

        # Step 3: Return the total number of students who couldn't eat
        return preference_count[0] + preference_count[1]

        # Alternative solution: efficient count and queue removal using pop(0) instead of unnecessary slicing
        # count = 0

        # while students:
        #     if students[0] == sandwiches[0]:
        #         students.pop(0)
        #         sandwiches.pop(0)
        #         count = 0  # Reset count as a sandwich was eaten
        #     else:
        #         students.append(students.pop(0))
        #         count += 1

        #     # If no one ate after a full cycle (number of students), stop
        #     if count == len(students):
        #         break

        # return len(students)

        # Unnecessary complex solution
        # retry = True
        # count = 0

        # while len(sandwiches) > 0 and retry != False:
        #     if students[0] == sandwiches[0]:
        #         students = students[1:]
        #         sandwiches = sandwiches[1:]
        #         count = 0
        #     else:
        #         if count <= len(students):
        #             students.append(students[0])
        #             students = students[1:]
        #             count += 1
        #         else:
        #             retry = False

        # return len(sandwiches)
