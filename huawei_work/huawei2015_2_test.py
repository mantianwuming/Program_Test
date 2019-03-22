# s = input()
# x = ''.join(sorted(set(s)))
# print(x)

s = input()
x = ''
for i in s:
    if i not in x:
        x += i
print(x)

def sort_str(s):
    s = list(s)
    for i in range(len(s)):
        for j in range(i,len(s)-1):
            if s[j] > s[j+1]:
                temp = s[j]
                s[j] = s[j+1]
                s[j+1] = temp
    x  = ''.join(s)
    return x

print(sort_str(x))
