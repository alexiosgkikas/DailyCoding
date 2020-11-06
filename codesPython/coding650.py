"""
This problem was asked by Google.
Let A be an N by M matrix in which every row and every column is sorted.
Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2].
For example, given the following matrix:
[[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]]

 And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 15 as there are 15 numbers in the matrix smaller than 6 or greater than 23.
"""



if __name__ == "__main__":
    N = 5
    M = 6
    A = [   [1, 3, 7, 10, 15, 20],
            [2, 6, 9, 14, 22, 25],
            [3, 8, 10, 15, 25, 30],
            [10, 11, 12, 23, 30, 35],
            [20, 25, 30, 35, 40, 45]
        ]

    i1 = 1
    j1 = 1
    i2 = 3
    j2 = 3
    
    smaller  = (i1+1)*(j1+1) - 1
    for i in range(i1+1,N):
        for j in range(0,j1):
            if A[i][j] < A[i1][j1]:
                smaller += 1
            else :
                continue

    for i in range(0,i1):
        for j in range(j1+1,M):
            if A[i][j] < A[i1][j1]:
                smaller += 1
            else :
                continue
             
    greater  = (M-i2)*(N-j2) -1


    for i in range(i2+1,N):
        for j in range(j2-1,-1,-1):
            if A[i][j] > A[i2][j2]:
                greater += 1
        else :
            continue

    for i in range(0,i2):
        for j in range(j2+1,M):
            if A[i][j] > A[i2][j2]:
                greater += 1
        else :
            continue
    
    print("smaller: ", smaller )
    print("greater: ", greater )
    print("sum: ", (greater+smaller) )


    
