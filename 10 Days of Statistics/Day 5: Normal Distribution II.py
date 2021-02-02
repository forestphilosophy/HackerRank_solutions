import math
mean, stdev = map(int,input().split())
threshold_80 = int(input())
threshold_60 = int(input())

cdf = 1 - 0.5*(1+math.erf((threshold_80-mean)/(stdev*math.sqrt(2))))
print (round(cdf*100,2))

cdf_higher_than_60 = 1 - 0.5*(1+math.erf((threshold_60-mean)/(stdev*math.sqrt(2))))
cdf_lower_than_60 = 0.5*(1+math.erf((threshold_60-mean)/(stdev*math.sqrt(2))))
print (round(cdf_higher_than_60*100,2))
print (round(cdf_lower_than_60*100,2))
