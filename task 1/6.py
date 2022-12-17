# title Squares
# description Вернуть элементы списка, отсортированного в неубываюшем порядке, возведенные в квадрат.
# ---end----

def squares(lst):
    ans = []
    i = 0

    while i < len(lst) and lst[i] < 0:
        i += 1
    if i == 0:
        for j in lst:
            ans.append(j**2)
    elif i == len(lst):
        for j in range(len(lst)-1, -1, -1):
            ans.append(lst[j]**2)
    else:
        neg = lst[:i]
        pos = lst[i:]
        ans_neg, ans_pos = [], []
        for j in range(len(neg)-1, -1, -1):
            ans_neg.append(lst[j]**2)
        for j in pos:
            ans_pos.append(j**2)
        ans = mergeLists(ans_neg, ans_pos)
    return ans



def mergeLists(a, b):
    ans = []
    i, j = 0,0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            ans.append(a[i])
            i += 1
        else:
            ans.append(b[j])
            j += 1
    if i < len(a):
        ans.extend(a[i:])
    if j < len(b):
        ans.extend(b[j:])
    return ans
