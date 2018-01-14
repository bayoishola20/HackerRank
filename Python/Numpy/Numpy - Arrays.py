import numpy

#===============================#
    # Code in stub above #
#===============================#

def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.array(arr[::-1], float)

#===============================#
    # Code in stub below #
#===============================#
arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)