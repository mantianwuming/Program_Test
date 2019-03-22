s = input()
# s1 = list(s)

# voc1 = ['(', '[', '{']
# voc2 = [')', ']', '}']
# def judge_s(s):
#     count1 = 0
#     count2 = 0
#     count3 = 0
#     for i in s:
#         if (i == ')' and count1 == 0) or (i == ']' and count2 == 0) or (i == '}' and count3 == 0):
#             return False
#         elif i == '(':
#             count1 += 1
#         elif i == ')':
#             count1 -= 1
#         elif i == '[':
#             count2 += 1
#         elif i == ']':
#             count2 -= 1
#         elif i == '{':
#             count3 += 1
#         elif i == '}':
#             count3 -= 1
#
#     if count1 == 0 and count2 == 0 and count3 == 0:
#         return True
#     else:
#         return False

def judge_rl(a, b):
    if a == '(' and b == ')':
        return 1
    if a == '[' and b == ']':
        return 1
    if a == '{' and b == '}':
        return 1
    else:
        return 0
def judge_s(s):
    x = []
    for i in s:
        if i == '(' or i == '[' or i == '{':
            x.append(i)
        elif i == ')' or i == ']' or i == '}':
            if x != [] and judge_rl(x[-1], i) == 1:
                return True
            else:
                return False
                break
print(judge_s(s))
