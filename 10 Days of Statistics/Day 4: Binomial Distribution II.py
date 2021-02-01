import math
def binom(n, k):
    return (math.factorial(n) / math.factorial(k) / math.factorial(n - k))

p,n = map(int,input().split())
p = p/100
ans = []
fianl_list = [[i for i in range(3)]]
list_2 = [i for i in range(2,n+1)]
fianl_list.append(list_2)

for i in range(2):
    pmf = [binom(n,k) * math.pow(p,k) * math.pow(1-p,n-k) for k in fianl_list[i]]
    print (round(sum(pmf),3))
