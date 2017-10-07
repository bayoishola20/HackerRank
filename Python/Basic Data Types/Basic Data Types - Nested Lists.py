students = []
for _ in xrange(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    students.append([name, score])

lowest_score = []
for i in xrange(len(students)):
    lowest_score.append(students[i][1])


second_lowest_score = []
for i in xrange(len(lowest_score)):
	if lowest_score[i] != min(lowest_score):
		second_lowest_score.append(lowest_score[i])

student = []
for i in xrange(len(students)):
    if students[i][1] == min(second_lowest_score):
        student.append(students[i][0])
student.sort()

for i in xrange(len(student)):
    print student[i]