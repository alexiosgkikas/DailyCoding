"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Facebook.
Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.
For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.
Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum
"""

def isSubsetSum(arr,n,sum):
    if sum==0:
        return True
    if n==0 and sum!=0:
        return False    
    if arr[n-1] > sum:
        return isSubsetSum(arr, n-1, sum)
    
    return isSubsetSum(arr, n-1, sum) or isSubsetSum(arr, n-1, sum-arr[n-1])

def partition(arr,n):
    if n==0:
        return False
    if sum(arr)%2 != 0:
        return False
    
    return isSubsetSum(arr, n, (sum(arr)/ 2))

if __name__ == "__main__":
    arr=[15, 5, 20, 10, 35, 15, 10]
    print(partition(arr,len(arr)))
    arr=[15, 5, 20, 10, 35]
    print(partition(arr,len(arr)))

