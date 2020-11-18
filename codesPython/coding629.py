"""
Daily Coding Problem: Problem #629 [Medium]
Good morning! Here's your coding interview problem for today.
This problem was asked by Etsy.
Given an array of numbers N and an integer k, your task is to split N into k partitions such that the maximum sum of any partition is minimized. Return this sum.
For example, given N = [5, 1, 2, 7, 3, 4] and k = 3, you should return 8, since the optimal partition is [5, 1, 2], [7], [3, 4].
"""
# code from https://www.geeksforgeeks.org/divide-the-array-in-k-segments-such-that-the-sum-of-minimums-is-maximized/
# Python 3 program to find the sum of
# the minimum of all the segments
MAX = 10
 
# Function to maximize the
# sum of the minimums
def maximizeSum(a,n, ind, k, dp):
    # If k segments have been divided
    if (k == 0):
        # If we are at the end
        if (ind == n):
            return 0
 
        # If we donot reach the end
        # then return a negative number
        # that cannot be the sum
        else:
            return -1e9
 
    # If at the end but
    # k segments are not formed
    elif (ind == n):
        return -1e9
 
    # If the state has been visited already
    elif (dp[ind][k] != -1):
        return dp[ind][k]
 
    # If the state has not been visited
    else:
        ans = 0
 
        # Get the minimum element 
        # in the segment
        mini = a[ind]
 
        # Iterate and try to break 
        # at every index
        # and create a segment
        for i in range(ind,n,1):
            # Find the minimum element 
            # in the segment
            mini = min(mini, a[i])
 
            # Find the sum of all the 
            # segments trying all
            # the possible combinations
            ans = max(ans, maximizeSum(\
             a, n, i + 1, k - 1, dp) + mini)
 
        # Return the answer by
        # memoizing it
        dp[ind][k] = ans
        return ans
         
# Driver Code
if __name__ == '__main__':
    a = [5, 7, 4, 2, 1, 6]
    k = 3
    n = len(a)
 
    # Initialize dp array with -1
    dp = [[-1 for i in range(MAX)]\
          for j in range(MAX)]
 
    print(maximizeSum(a, n, 0, k, dp))
 
# This code is contributed by
# Surendra_Gangwar