N, M = int(raw_input()), raw_input().split()
print (any([(i == i[::-1]) for i in M]) and all([(int(j) > 0) for j in M]))