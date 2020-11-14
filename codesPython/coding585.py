"""
Daily Coding Problem: Problem #585 [Medium] 
Good morning! Here's your coding interview problem for today.
This question was asked by Google.
Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing only 1's and return its area.
For example, given the following matrix:
[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]
Return 4.
"""

def find_rectangle(rectangles,idx_row,idx_col,value):
    #print("starting point: ",(idx_row,idx_col))
    max_row = idx_row
    for row in range(idx_row,len(rectangles)):
        if rectangles[row][idx_col] == 1:
            rectangles[row][idx_col] = value
            max_row = row
        else:
            continue
    max_col = idx_col
    for col in range(idx_col,len(rectangles[idx_row])):
        if rectangles[idx_row][col] == 1:
            rectangles[idx_row][col] = value
            max_col = col
        else:
            continue
    
    for i in range (idx_row+1,max_row+1):
        for j in range (idx_col+1,max_col+1):
            rectangles[i][j] = value

    #print("area: ",(max_row-idx_row+1)* (max_col-idx_col+1))
    return rectangles, value,((max_row-idx_row+1)* (max_col-idx_col+1))



def find_max_area(rectangles):
    value = 2
    max_area = 0
    for idx_row in range(0,len(rectangles)):
        for idx_col in range(0,len(rectangles[0])):
            if rectangles[idx_row][idx_col] == 1:
               rectangles,value,area =  find_rectangle(rectangles,idx_row,idx_col,value)
               max_area = max(max_area,area)
               value+=1
    #print(rectangles)
    return max_area             


if __name__ == "__main__":
    rectangles = [
        [1, 0, 0, 0],
        [1, 0, 1, 1],
        [1, 0, 1, 1],
        [0, 1, 0, 0]
        ]

    print(find_max_area(rectangles))