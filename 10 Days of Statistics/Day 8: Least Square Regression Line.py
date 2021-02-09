import statistics

X = []
Y = []
for i in range(5):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

num_of_vals = len(X)
X_stdev = statistics.stdev(X)
Y_stdev = statistics.stdev(Y)
X_mean = statistics.mean(X)
Y_mean = statistics.mean(Y)

rho = sum([(x - X_mean)* (y - Y_mean) for x,y in zip(X,Y)]) / (num_of_vals * X_stdev * Y_stdev)

b = rho * X_stdev / Y_stdev
a = Y_mean - b * X_mean

result = a + b * 80
print (round(result,3))
