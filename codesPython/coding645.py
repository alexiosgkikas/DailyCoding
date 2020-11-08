"""
Daily Coding Problem: Problem #645 [Easy]
Good morning! Here's your coding interview problem for today.
This problem was asked by Microsoft.
Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.
For example, given the following matrix:
[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.
"""
def check_word_row(array,target):
    if len(target) == 0:
        return True
    
    if len(array)<=0 or array[0] != target[0] :
        return False
    return check_word_row(array[1:],target[1:])

def check_word_col(array,row,col,target):
    if len(target) == 0:
        return True
    if row>=len(array) or col>=len(array[row]) or array[row][col] != target[0] :
        return False
    return check_word_col(array,row+1,col+1,target[1:])


def search(array,target):
    if len(target) == 0:
        return False
    for i in range(0,len(array)):
        for j in range(0,len(array[0])-len(target)+1):
            if check_word_row(array[i][j:],target) or check_word_col(array,i,j,target):
                return True
    return False


if __name__ == "__main__":
    array = [
        ['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']
        ]
    target_word = 'MASS'
    print(search(array,target_word))



