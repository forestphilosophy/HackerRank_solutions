import math
mean, stdev = map(int,input().split())
threshold = float(input())
threshold_L, threshold_H = map(int,input().split())

cdf = 0.5*(1+math.erf((threshold-mean)/(stdev*math.sqrt(2))))
print (round(cdf,3))

cdf_L = 0.5*(1+math.erf((threshold_L-mean)/(stdev*math.sqrt(2))))
cdf_H = 0.5*(1+math.erf((threshold_H-mean)/(stdev*math.sqrt(2))))
print (round(cdf_H-cdf_L,3))
