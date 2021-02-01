import math
nom,dem = map(int,input().split())
p = nom / dem
x = int(input())

pdf = math.pow(1-p,x-1)*p

print (round(pdf,3))
