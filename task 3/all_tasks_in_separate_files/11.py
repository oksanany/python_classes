# если нужны только четные, возведенные в квадрат
ans = [i**2 for i in range(2,28,2)]
print(ans)

# если нужны все числа, но четные, возведенные в квадрат
ans = [i**2 if i % 2 == 0 else i for i in range(2,28)]
print(ans)