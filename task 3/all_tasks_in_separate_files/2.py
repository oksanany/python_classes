# solution 2.0
ans = [i for i in range(1,1001) if str(2) in str(i)]

# solution 2.1
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

# solution 2.2
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



