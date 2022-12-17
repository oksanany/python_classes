# 1
# ---------
ans = [i for i in range(17,1001, 17)]
print(ans)
# ---------


# 2
# ---------
## 2.0
ans = [i for i in range(1,1001) if str(2) in str(i)]
print(ans)


## 2.1
ans = list(range(200,300))
ans.extend([list(range(int(str(i) + str(20)), int(str(i)+str(30)))) for i in range(1,10)])
ans = []
i = 2
while i <= 1000:
    h = i // 100
    d = (i - h*100) // 10
    e = (i - h*100) % 10
    if h == 2:
        ans.extend(list(range(200, 300)))
        i += 100
    elif d == 2:
        start = int(str(h) + str(20))
        end = int(str(h) + str(30))
        ans.extend(list(range(start, end)))
        i += 10
    else:
        ans.append(i)
        i += 10
print(ans)

# 2.2
ans = [2]
med = [int(str(i) + str(2)) for i in range(1,10) if i != 2]
ans.extend(med)
ans.extend(list(range(20,30)))
ans.extend(list(range(200,300)))
med = [int(str(i)+str(j)+str(2)) for i in range(1,10) for j in range(0,10) if i != 2 and j != 2]
ans.extend(med)
med = [j for k in[list(range(int(str(i) + str(20)), int(str(i)+str(30)))) for i in range(1,10) if i != 2] for j in k]
ans.extend(med)
ans.sort()
print(ans)
# ---------


# 3
# ---------
ans = [int(str(i)*2) for i in range(1,10)]
ans.extend([int(str(j)+str(i)+str(j)) for j in range(1,10) for i in range(10)])
ans.extend([int(str(j)+str(i)*2 + str(j)) for j in range(1,10) for i in range(10)])
print(ans)
# ---------


# 4
# ---------
string = input()
print(string.count(' '))
# ---------


# 5
# ---------
vowels = 'aoeiuy'
vowels += vowels.upper()
string = input()
ans = ''.join([s for s in string if s not in vowels])
print(ans)
# ---------


# 6
# ---------
ans = [word for word in input().split(' ') if len(word) <= 5]
print(ans)
# ---------

# 7
# ---------
ans = {word: len(word) for word in input().split(' ')}
print(ans)
# ---------

# 8
# ---------
string = input().replace(' ', '')
ans = list(set(string))
print(ans)
# ---------

# 9
# ---------
nums = [int(x) for x in input().split()]
ans = list(map(lambda x: x**2, nums))
print(ans)
# ---------

# 10
# ---------
def belongsToLine(coord):
    ans = {(i,j): (i**2 + j**2)**(1/2) for i,j in coord if j == 5*i - 2}
    return ans
# ---------

# 11
# ---------
## если нужны только четные, возведенные в квадрат
ans = [i**2 for i in range(2,28,2)]
print(ans)

## если нужны все числа, но четные, возведенные в квадрат
ans = [i**2 if i % 2 == 0 else i for i in range(2,28)]
print(ans)
# ---------

# 12
# ---------
def farthestPoint(coord):
    ans = [(i**2 + j**2)**(1/2) for i,j in coord if i > 0 and j > 0]
    return max(ans)
# ---------

# 13
# ---------
def sumsDiffs(first, second):
    ans = [(first[i] + second[i], first[i] - second[i]) for i in range(len(first))]
    return ans
print(sumsDiffs([1, 2, 3, 5, 8], [2, 4, 8, 16, 32]))
# ---------

# 14
# ---------
def evenSq(lst):
    ans = [str(int(i)**2) for i in lst if int(i[-1]) % 2 == 0]
    return ans
print(evenSq(['43141', '32441', '431', '4154', '43121']))
# ---------

# 15
# ---------
def to_json(input_str):
    lst = [i.split(',') for i in input_str.split(' ')]
    titles = [i[0] for i in lst]
    values = [[lst[j][i] for j in range(len(lst))]for i in range(1,len(lst[0]))]
    return [dict(zip(titles, values[i])) for i in range(len(values))]

print(to_json("""name,Petya,Vasya,Masha,Vova grade,5,5,8,3 subject,math,language,physics,math year,1999,2000,1995,1998"""))
# ---------

# 16
# ---------
def sumCols(mat):
    res = [sum(row[column] for row in mat) for column in range(len(mat[0]))]
    return res

print(sumCols([[11.9, 12.2, 12.9], [15.3, 15.1, 15.1], [16.3, 16.5, 16.5], [17.7, 17.5, 18.1]]))
# ---------


