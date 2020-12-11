"""
Daily Coding Problem: Problem #673 [Hard]
Good morning! Here's your coding interview problem for today.
This problem was asked by LinkedIn.
Given a list of points, a central point, and an integer k, find the nearest k points from the central point.
For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].
"""

def distance(p1,p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 


def nearest_points(points,cp,k):
    near_points = []

    if len(points) <= k:
        return points

    for p in points:
        near_points.append((p[0],p[1],distance(p,cp)))

    near_points.sort(key=lambda d:d[2])
    return [(p[0],p[1]) for p in near_points[:k]]


    
    
def main():
    points =  [(0, 0), (5, 4), (3, 1)]
    cp = (1,2)
    k = 2
    print(nearest_points(points,cp,k))


if __name__ == "__main__":
    main()
