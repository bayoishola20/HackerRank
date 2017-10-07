# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
n_set = set(raw_input().split()) #split: to split characters

b = int(raw_input())
b_set = set(raw_input().split()) #split: to split characters

print len(b_set.intersection(n_set))