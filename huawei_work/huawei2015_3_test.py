x = int(input())

def count_x(before, des, res, ex):
    if before == 0:
        if des == res:
            return 1
        else:
            return 0
    else:
        return count_x(before-1, before, res+des, 1) + count_x(before-1, before, res-des,1) + count_x(before-1, before*10**ex+des, res, ex+1)

print(count_x(8,9,x,1))
