#In Python 2, the expression input() is equivalent to eval(raw _input(prompt)).
x, k = map(int, raw_input().split())
print input() == k