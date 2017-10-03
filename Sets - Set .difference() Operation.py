# Enter your code here. Read input from STDIN. Print output to STDOUT

n = raw_input()
n_set = set(raw_input().split()) #split: to split characters

b = raw_input()
b_set = set(raw_input().split()) #split: to split characters

print len(n_set.difference(b_set))