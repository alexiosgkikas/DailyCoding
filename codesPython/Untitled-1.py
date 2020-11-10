"""
Daily Coding Problem: Problem #600 [Easy] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
Given a set of points (x, y) on a 2D cartesian plane, find the two closest points. For example, given the points [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)], return [(-1, -1), (1, 1)].
"""

def distance(x1,y1,x2,y2):
    return sqrt(pow(x1-x2,2)+pow(y1-y2,2))


def find_min_distance(points):
    mini = None
    distance = 2147483647
    for i in range(0,len(points)):
        for j in range(i+1:len(points)):
            dist = distance(points[i][0],points[i][1],points[j][0],points[j][1])
            if  dist < distance:
                distance = dist
                mini = [points[i],points[j]]
    return mini



if __name__ == "__main__":
    points = [[(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]]
