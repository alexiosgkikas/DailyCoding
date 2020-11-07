"""
Daily Coding Problem: Problem #498 [Easy] 
This problem was asked by WhatsApp.
Given an array of integers out of order, determine the bounds of the smallest window that must be sorted in order for the entire array to be sorted. For example, given [3, 7, 5, 6, 9], you should return (1, 3).

"""

def boundries(arr):
    min_b = len(arr)
    max_b = 0

    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                if min_b > j:
                    min_b = j
                if max_b < j+1:
                    max_b = j+1
                
    if  min_b>max_b:
        return (0,0)
    return (min_b,max_b)

if __name__ == "__main__":
    arr =[3, 7, 5, 6, 9]
    print(boundries(arr))
    