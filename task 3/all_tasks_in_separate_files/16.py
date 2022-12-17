def sumCols(mat):
    res = [sum(row[column] for row in mat) for column in range(len(mat[0]))]
    return res

print(sumCols([[11.9, 12.2, 12.9], [15.3, 15.1, 15.1], [16.3, 16.5, 16.5], [17.7, 17.5, 18.1]]))