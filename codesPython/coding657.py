"""
Daily Coding Problem: Problem #657 [Easy] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
You may also use a list or array to represent a set.
"""
import math
# code base on https://www.geeksforgeeks.org/recursive-program-to-generate-power-set/
def power_set(set_list):
    max_size = int(math.pow(2,len(set_list)))
    ps = [] # list that hold power set
    for i in range(0,max_size):
        ls = []
        for j in range(0,len(set_list)):
            if (i & 1 << j) >0:
               ls.append(set_list[j])
        ps.append(ls)
    
    return ps

if __name__ == '__main__':
    set_list = [1,2,3]
    print(power_set(set_list))

