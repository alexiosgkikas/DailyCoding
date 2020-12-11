"""
Daily Coding Problem: Problem #373 [Hard]
Good morning! Here's your coding interview problem for today.
This problem was asked by Facebook.
Given a list of integers L, find the maximum length of a sequence of consecutive numbers that can be formed using elements from L.
For example, given L = [5, 2, 99, 3, 4, 1, 100], return 5 as we can build a sequence [1, 2, 3, 4, 5] which has length 5.
"""

def max_seq(array):
    array = list(set(array))
    array.sort()
    print(array)
    start_index , end_index = 0,1
    count = 1
    for i in range(1,len(array)):
        if array[i] -1  == array[i-1]:
            count +=1
        else:
            if (end_index-start_index) < count:
                end_index = i 
                start_index = end_index - count 
                count = 1

    print(start_index , end_index)
    return end_index - start_index


if __name__ == "__main__":
    L = [5, 2, 99, 3, 4, 1, 100,101,102,103,104,105,107]
    print(max_seq(L))

