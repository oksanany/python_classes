# title Sum Ranges
# description Напечатать все последовательности из списка.
# ---end----

def sumRanges(lst):
    ans = []
    s = lst[0]
    m = lst[0]
    for i in range(1,len(lst)):
        if lst[i] == m + 1:
            m += 1
            continue
        else:
            f = lst[i-1]
            ans.append((s,f))
            s = lst[i]
            m = s
    f = m
    ans.append((s,f))
    answer = []
    for i,j in ans:
        if i != j:
            answer.append(str(i) + "->" + str(j))
        else:
            answer.append(str(i))
    return answer



