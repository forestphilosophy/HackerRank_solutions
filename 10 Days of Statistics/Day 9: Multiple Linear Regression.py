from sklearn import linear_model
m,n = map(int,input().split())

x = []
y = []
for i in range(n):
    *X,Y = list(map(float,input().split()))
    x.append(X)
    y.append(Y)
  
lm = linear_model.LinearRegression()
lm.fit(x, y)
a = lm.intercept_
b = lm.coef_

q = int(input())
for i in range(q):
    ans = 0
    vals = list(map(float,input().split()))
    for j in range(m):   
        ans += vals[j] * b[j]
    ans += a
    print (ans)
