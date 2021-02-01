import math
nom,dem = map(int,input().split())
p = nom / dem
x = int(input())

arr = [i for i in range(1,x+1)]
pdf = [math.pow(1-p,x-1)*p for x in arr]

print (round(sum(pdf),3))
