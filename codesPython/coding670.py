"""
Daily Coding Problem: Problem #670 [Medium] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Facebook.
Given a positive integer n, find the smallest number of squared integers which sum to n.
For example, given n = 13, return 2 since 13 = 3^2 + 2^2 = 9 + 4.
Given n = 27, return 3 since 27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9.
"""



import math 

def smallest_squared_number1(num):
    dp = [None] * (num+1)

    dp[0],dp[1],dp[2],dp[3] = 0,1,2,3

    for i in range(4,num+1):
        dp[i] = i
        for j in range(1,i+1):
            temp = j*j
            if temp > i:
                break
            else:
               dp[i] = min(dp[i],1+dp[temp])
    return  dp[num]


def smallest_squared_number2(num):
    if num < 4 :
        return  num
    
    res  =  num

    for x in range (1,num+1):
        temp = x*x
        if temp > num:
            break
        else:
            res = min(res,1+smallest_squared_number2(num-temp))

    return res

            

if __name__ == "__main__":
    print(smallest_squared_number1(13))
    print(smallest_squared_number2(27))
    
