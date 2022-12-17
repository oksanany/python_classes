ans = [int(str(i)*2) for i in range(1,10)]
ans.extend([int(str(j)+str(i)+str(j)) for j in range(1,10) for i in range(10)])
ans.extend([int(str(j)+str(i)*2 + str(j)) for j in range(1,10) for i in range(10)])
print(ans)