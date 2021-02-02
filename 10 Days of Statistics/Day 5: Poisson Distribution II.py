import math
mean_A, mean_B = map(float,input().split())

expected_value_A = 160+ 40*(mean_A + math.pow(mean_A,2))
expected_value_B = 128+ 40*(mean_B + math.pow(mean_B,2))

print (round(expected_value_A,3))
print (round(expected_value_B,3))
