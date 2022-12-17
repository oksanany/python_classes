# title Compress list
# description Повторяющиеся буквы записывать как букву и количество повторений.
# ---end----


def compress(lst):
    l = lst[0]
    s = 1
    ans = l
    for i in range(1, len(lst)):
        if lst[i] == l:
            s+=1
        else:
            if s > 1:
                ans += str(s)
            ans += lst[i]
            s = 1
            l = lst[i]
    if s > 1:
        ans += str(s)
    return ans

print(compress(["c","c","c"]))