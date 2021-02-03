import math
max_weight = int(input())
num_of_boxes = int(input())
sample_mean = int(input())
sample_std = int(input())

population_mean = sample_mean * num_of_boxes
population_std = sample_std * math.sqrt(num_of_boxes)
cdf = 0.5*(1+math.erf((max_weight-population_mean)/(population_std*math.sqrt(2))))
print (round(cdf,4))
