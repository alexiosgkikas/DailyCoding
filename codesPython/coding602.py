"""
Daily Coding Problem: Problem #602 [Easy]
Good morning! Here's your coding interview problem for today.
This problem was asked by Facebook.
Suppose you are given two lists of n points, one list p1, p2, ..., pn on the line y = 0 and the other list q1, q2, ..., qn on the line y = 1. Imagine a set of n line segments connecting each point pi to qi. Write an algorithm to determine how many pairs of the line segments intersect.
"""

def intersect(p1,q1,p2,q2):
    if (p1 < p2 and q1 > q2) or (p1 > p2 and q1 < q2):
        return True
    return False

def pairs_intesect(list1,list2):
    if len(list1) != len(list2):
        return None
    
    n = len(list1)
    count =0
    for i in range(0,n):
        for j in range(i,n):
            if intersect(list1[i],list2[i],list1[j],list2[j]):
                count+=1
                #print("pair {},{} - {},{} intersect".format(list1[i],list2[i],list1[j],list2[j]))
    return count

if __name__ == "__main__":
    list1 = [1,1,2,3,4]
    list2 = [1,2,1,5,0]
    print(pairs_intesect(list1,list2))