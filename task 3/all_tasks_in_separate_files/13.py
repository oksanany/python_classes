def sumsDiffs(first, second):
    ans = [(first[i] + second[i], first[i] - second[i]) for i in range(len(first))]
    return ans
print(sumsDiffs([1, 2, 3, 5, 8], [2, 4, 8, 16, 32]))
