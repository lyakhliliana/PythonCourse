n = int(input())
students = []
for i in range(n):
    student, mark = input().split()
    students.append((student, int(mark)))
students.sort(key=lambda x: x[1], reverse=True)
for i in range(n):
    print(students[i][0])
