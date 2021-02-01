num_of_vals = input()
vals = list(map(int,input().split()))
freq = list(map(int,input().split()))

weighted_avg = sum([x*y for x,y in zip(vals,freq)])/sum(freq)
print (round(weighted_avg,1))
