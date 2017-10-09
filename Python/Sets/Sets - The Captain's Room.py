# Enter your code here. Read input from STDIN. Print output to STDOUT

K = int(raw_input())
room_numbers = (map(int, raw_input().split()))

captain_room = (K * sum(set(room_numbers)) - sum(room_numbers)) // (K - 1)

print captain_room