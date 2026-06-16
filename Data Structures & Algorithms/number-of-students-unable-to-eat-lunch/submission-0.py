class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    
        counter = 0

        while len(students) != counter:
            if students[0] == sandwiches[0]:
                del students[0]
                del sandwiches[0]
                counter = 0
            else:
                k = students.pop(0)
                students.append(k)
                counter += 1

        return len(students)