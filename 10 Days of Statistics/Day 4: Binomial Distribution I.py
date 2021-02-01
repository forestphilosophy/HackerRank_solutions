import math
def binom(n, k):
    return (math.factorial(n) / math.factorial(k) / math.factorial(n - k))

val1,val2 = map(float,input().split())
n = 6
k = [3,4,5,6]
p = val1 / (val1+val2)
pmf = [binom(n,k) * math.pow(p,k) * math.pow(1-p,n-k) for k in k]

print (round(sum(pmf),3))
