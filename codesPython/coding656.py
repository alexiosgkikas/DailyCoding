"""
Daily Coding Problem: Problem #656 [Medium] 
Good morning! Here's your coding interview problem for today.
Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.
For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:
B B W
W W W
W W W
B B B
Becomes
B B G
G G G
G G G
B B B
"""

def change_color(image, p, new):
    row = p[0]-1
    col = p[1]-1
    old = image[row][col]
    min_row = max(0,row-1)
    max_row = min(len(image)-1,row+1)
    min_col = max(0,col-1)
    max_col = min(len(image[0])-1,col+1)
    for i in range(min_row,max_row+1):
        for j in range(min_col,max_col+1):
            if image[i][j] is old:
                image[i][j] = new
    
    #return image


if __name__ == "__main__":
    image = [
        ['B','B','W'],
        ['W','W','W'],
        ['W','W','W'],
        ['B','B','B']
    ]
    change_color(image, (3,3), 'G')
    print(image)