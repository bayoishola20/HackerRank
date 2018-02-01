import math
max_weight = float(raw_input())
N = int(raw_input())
mean = float(raw_input())
std = float(raw_input())

def cum_dist(mean, std, x):
    return (0.5) * (1 + math.erf((x - mean) / (std * (math.sqrt(2)))))

mean *= N #new mean
std *= math.sqrt(N) #new std


print round(cum_dist(mean, std, max_weight), 4)