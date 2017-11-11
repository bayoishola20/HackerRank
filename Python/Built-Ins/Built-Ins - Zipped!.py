# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = map(int, raw_input().split())

subjects = []

for i in xrange(X):
    subjects.append(map(float, raw_input().split()))
students_scores = zip(*subjects)

for j in xrange(N):
    average_score = 0.0
    for k in xrange(X):
        average_score += students_scores[j][k]
    print average_score/X