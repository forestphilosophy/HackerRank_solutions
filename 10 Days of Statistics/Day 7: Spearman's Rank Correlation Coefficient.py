import math
import statistics

num_of_vals = int(input())
X = list(map(float,input().split()))
Y = list(map(float,input().split()))

def get_ranks(arr):
    temp = {}
    rank = 1
    for i in sorted(arr):
        if i not in temp:
            temp[i] = rank
            rank += 1
    temp = [(k,temp[k]) for k in arr]
    r_x = [y for x,y in temp]
    return r_x 

r_x = get_ranks(X)
r_y = get_ranks(Y)
d = [x - y for x,y in zip(r_x,r_y)]

rho = 1 - 6 * sum([math.pow(i,2) for i in d]) / (num_of_vals * (math.pow(num_of_vals,2)-1))

print (round(rho,3))
