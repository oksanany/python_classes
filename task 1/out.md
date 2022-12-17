+ [Print Hello World](#print-hello-world)
+ [Ones](#ones)
+ [Sum Ranges](#sum-ranges)
+ [Diagonal Sum](#diagonal-sum)
+ [Merge Sorted Lists](#merge-sorted-lists)
+ [Squares](#squares)
+ [Compress list](#compress-list)
--------------------------------

## Print Hello World

Напечатать на экран hello, если число делится на 3; world, если число делаится на 5, и само число, иначе.

```python
def helloWorld(n):
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print('hello, world!')
        elif i % 3 == 0:
            print('hello', end = '')
        elif i % 5 == 0:
            print('world', end='')
        else:
            print(i)
```

## Ones

Найти длину максимальной непрерывной подпоследовательности, состоящей из 1.

```python
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
```

## Sum Ranges

Напечатать все последовательности из списка.

```python
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




```

## Diagonal Sum

Посчитать сумму элементов на главной и побочной диагоналях.

```python
def diagonalSum(mat):
    result = 0
    n = len(mat)
    for i in range(n):
        result += mat[i][i]
        result += mat[i][n - i - 1]
        if n % 2 != 0 and i == n // 2:
            result -= mat[i][n - i - 1]

    return result

mat1 = [[1,2,3],
       [4,5,6],
       [7,8,9]]

print(diagonalSum(mat1))
```

## Merge Sorted Lists

Получить один отсортированный массив из двух отсортированных.

```python
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






```

## Squares

Вернуть элементы списка, отсортированного в неубываюшем порядке, возведенные в квадрат.

```python
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

```

## Compress list

Повторяющиеся буквы записывать как букву и количество повторений.

```python
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
```