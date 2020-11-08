"""
Daily Coding Problem: Problem #569 [Hard]
Good morning! Here's your coding interview problem for today.
This problem was asked by Facebook.
Given an array of numbers of length N, find both the minimum and maximum using less than 2 * (N - 2) comparisons.
"""

def find_min_max(arr):
    comp =0
    mini ,maxi = arr[0],arr[1]

    



   
    return  arr[0], arr[len(arr)-1] 
if __name__ == "__main__":
    arr = [10,1,65,22,-2,99,7,22,-10]
    print(find_min_max(arr))


