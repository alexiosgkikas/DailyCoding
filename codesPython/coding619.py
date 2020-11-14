"""
Daily Coding Problem: Problem #619 [Easy] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Coursera.
Given a 2D board of characters and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
For example, given the following board:
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
"""
import copy

def find_next_letter(board,word,row,col):
    # if no other character exist ,we fullfilled word and return True 
    if len(word) == 0:
        return True
    #if row or column is out of grid return False
    if row not in range(0,len(board)) or col not in range(0,len(board[row])):
        return False

    #if cell exist(in grid) change value to True(as visited) and check for neighborhood cells (up,bottom,left,right)
    if board[row][col] and board[row][col] == word[0]:
        board[row][col] = True
        return (
            find_next_letter(copy.deepcopy(board),word[1:],row-1,col) 
            or find_next_letter(copy.deepcopy(board),word[1:],row+1,col) 
            or find_next_letter(copy.deepcopy(board),word[1:],row,col-1)
            or find_next_letter(copy.deepcopy(board),word[1:],row,col+1)
        )
    else:
        return False

def word_exist(board,word):
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if board[i][j] == word[0]:
                if find_next_letter(copy.deepcopy(board),word,i,j):
                    return True
    return False


if __name__ == '__main__':
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    
    print(word_exist(board,"ABCCED"))
    print(word_exist(board,"SEE"))
    print(word_exist(board,"ABCB"))
