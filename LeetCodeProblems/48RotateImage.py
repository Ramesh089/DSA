# ..................................Brute force solution..........................

def rotate(matrix):
    n = len(matrix)
    ans = [[0] * n for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            ans[j][len(matrix)-1-i] = matrix[i][j]


    return ans


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))


# .............................................Opatimal solution.......................................
def rotate(matrix):
    n = len(matrix)
    for i in range(n-1):
        for j in range(i+1,n-1):
            matrix[i][j] = matrix[j][i],matrix[i][j]

    for i in range(n):
        matrix[i].reverse()

    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))