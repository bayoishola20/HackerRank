sizes = list(map(int, raw_input().split()))
X = list(map(int, raw_input().split()))
F = list(map(int, raw_input().split()))

def with_freq(X, F):       
    freq_list = []
    for i, x in enumerate(X):
        freq_list.extend([x] * F[i])
    return freq_list


X, F = zip(*sorted(zip(X, F), key=lambda x: x[0]))

nums = with_freq(X, F)

def median(nums):       
    size = len(nums)    
    if size % 2:
        return float(nums[size/2])
    else:
        return sum(nums[size/2-1:size/2+1])/2.0

def quartiles(nums):       
    total = len(nums)
    
    if total == 1:
        print nums[0]
        print nums[0]
        print nums[0]

    else:
        odd = total % 2        

        q1 = median(nums[:total/2])
        q2 = median(nums)
        q3 = median(nums[total/2 + 1 if odd else total/2:])

        return q1, q2, q3

q1, q2, q3 = quartiles(nums)
print q3 - q1