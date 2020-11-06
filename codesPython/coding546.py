"""
Daily Coding Problem: Problem #546 [Medium]
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.
For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:
•	There is 1 smaller element to the right of 3
•	There is 1 smaller element to the right of 4
•	There are 2 smaller elements to the right of 9
•	There is 1 smaller element to the right of 6
•	There are no smaller elements to the right of 1
"""

def smaller_right(array):
    ls = [0] * len(array)
    for i in range(0,len(array)):
        print("check for ",array[i])
        for j in range(i+1,len(array)):
            if array[i] > array[j]:
                ls[i] +=1
    return ls


if __name__ == "__main__":
    print( smaller_right([3, 4, 9, 6, 1]) )
