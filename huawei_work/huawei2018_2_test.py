import numpy as np
m,n = map(int, input().split())
x = np.zeros((m,n))
for i in range(m):
    x[i] = list(map(int,input().split()))

def max_x(m,n,x):
    if m == n == 0:
        return x[0][0]
    if m == 0:
        return x[m][n] + max_x(m, n-1, x)
        # print(res)
    if n == 0:
        return x[m][n] + max_x(m-1, n, x)
        # print(res)
    else:
        return max(x[m][n] + max_x(m-1,n,x), x[m][n] + max_x(m, n-1, x))

def max_x(m,n,x):
    if m == 0 and n == 0:
        return x[0][0]
    elif m == 0:
        return x[m][n] + max_x(m, n-1, x)
    elif n == 0:
        return x[m][n] + max_x(m-1, n ,x)
    else:
        return max(x[m][n] + max_x(m, n-1, x), x[m][n] + max_x(m-1, n, x))

res = max_x(m-1,n-1,x)
print(res)
