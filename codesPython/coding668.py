"""
Daily Coding Problem: Problem #668 [Easy]
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.
Here is an example:
1 2 3 4 8
5 1 2 3 4
4 5 1 2 3
7 4 5 1 2
Write a program to determine whether a given input is a Toeplitz matrix.
"""

def isToeplitz(array):
    for row in range(1,len(array)):
        if array[row-1][0:-1] != array[row][1:]:
            return False
    return True

if __name__ == "__main__":
    array = [
        [1,2,3,4,8],
        [5,1,2,3,4],
        [4,5,1,2,3],
        [7,4,5,1,2]
    ]

    print(isToeplitz(array))