import math
values = list(map(float, raw_input().split()))
mean = values[0]
std = values[1]
first = float(raw_input())
second = list(map(float, raw_input().split()))
second_lower = second[0]
second_upper = second[1]

def cum_dist(mean, std, x):
    return (0.5) * (1 + math.erf((x - mean) / (std * (math.sqrt(2)))))

print round(cum_dist(mean, std, first) , 3)
print round(cum_dist(mean, std, second_upper) - cum_dist(mean, std, second_lower) , 3)