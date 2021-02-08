import math
import statistics

num_of_vals = int(input())
X = list(map(float,input().split()))
Y = list(map(float,input().split()))

X_stdev = statistics.pstdev(X)
Y_stdev = statistics.pstdev(Y)
X_mean = statistics.mean(X)
Y_mean = statistics.mean(Y)

rho = sum([(x - X_mean)* (y - Y_mean) for x,y in zip(X,Y)]) / (num_of_vals * X_stdev * Y_stdev)

print (round(rho,3))
