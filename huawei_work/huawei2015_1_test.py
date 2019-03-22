alist = list(input().split(','))
# print(m,n)
# slist = list(input().split(','))
# print(alist)

# print(alist)

def output_str(a_str,n):
    if len(a_str) <= n:
        while len(a_str) < n:
            a_str += '0'
        # slist.append(a_str)
        # return a_str
        print(a_str)
    else:
        print(a_str[:n])
        a_str = a_str[n:]
        output_str(a_str,n)

m = int(alist[0])
n = int(alist[1])
alist = alist[2:]
for i in range(m):
    output_str(alist[i],n)
    # xlist += slist

# print(xlist)
