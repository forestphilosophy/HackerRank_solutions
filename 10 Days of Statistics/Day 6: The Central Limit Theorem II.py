import math
num_of_tickets = int(input())
num_of_students = int(input())
sample_mean = float(input())
sample_std = float(input())

population_mean = sample_mean * num_of_students
population_std = sample_std * math.sqrt(num_of_students)
cdf = 0.5*(1+math.erf((num_of_tickets-population_mean)/(population_std*math.sqrt(2))))
print (round(cdf,4))
