"""
Daily Coding Problem: Problem #641 [Easy] 
This problem was asked by Amazon.
Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.
For example, for the input [1, 2, 3, 10], you should return 7.
Do this in O(N) time.
"""

def minimum(arr ,length):
    result=1
    for i in range(0,length):
        if arr[i]<=result:
            result=result+arr[i]
        else:
            break
    return result 

if __name__ == "__main__":
    arr=[1, 2, 3, 10]
    print(minimum( arr , len(arr)))