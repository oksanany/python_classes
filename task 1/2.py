# title Ones
# description Найти длину максимальной непрерывной подпоследовательности, состоящей из 1.
# ---end----

def ones(lst):
    c = 0
    c_max = 0
    for i in lst:
        if i == 1:
            c += 1
        else:
            if c > c_max:
                c_max = c
            c = 0
    if c > c_max:
        c_max = c
    return c_max