import math
sample_size = int(input())
mean = int(input())
stdev = int(input())
confidence_interval = float(input())
z_score = float(input())

A = mean - z_score * stdev / math.sqrt(sample_size)
B = mean + z_score * stdev / math.sqrt(sample_size)
print (A)
print (B)
