# title Merge Sorted Lists
# description Получить один отсортированный массив из двух отсортированных.
# ---end----


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





