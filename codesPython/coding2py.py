"""
Daily Coding Problem: Problem #2 [Hard]
Good morning! Here's your coding interview problem for today.
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
"""

def product(arr):
    prod = 1
    ls =[]
    for i in range(0,len(arr)):
        prod*=arr[i]
    
    for i in range(0,len(arr)):
        ls.append((int)(prod/arr[i]))
    
    return ls

# Follow-up: what if you can't use division?
def product2(arr):
    ls = []
    for i in range(0,len(arr)):
        prod = 1
        for j in range(0,len(arr)):
            if i!=j:
                prod*= arr[j]
        ls.append(prod)
    
    return ls

if __name__ == "__main__":
    print(product2([1, 2, 3, 4, 5]))
    print(product2([3, 2, 1]))

