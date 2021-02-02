import math
mean = float(input())
k = int(input())

pdf = math.pow(mean,k)*math.exp(-mean)/math.factorial(k)
print (round(pdf,3))
