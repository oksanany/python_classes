# title Diagonal Sum
# description Посчитать сумму элементов на главной и побочной диагоналях.
# ---end----


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