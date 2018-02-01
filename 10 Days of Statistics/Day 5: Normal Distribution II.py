import math
values = list(map(float, raw_input().split()))
mean = values[0]
std = values[1]
first = float(raw_input())
second_third = float(raw_input())

def cum_dist(mean, std, x):
    return (0.5) * (1 + math.erf((x - mean) / (std * (math.sqrt(2)))))

print round(100 - cum_dist(mean, std, first)*100 , 2)
print round(100 - cum_dist(mean, std, second_third)*100 , 2)
print round(cum_dist(mean, std, second_third)*100 , 2)