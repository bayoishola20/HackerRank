values = list(map(float, raw_input().split()))
mean_A = values[0]
mean_B = values[1]

print round((160 + 40*(mean_A + mean_A**2)),3)
print round((128 + 40*(mean_B + mean_B**2)),3)