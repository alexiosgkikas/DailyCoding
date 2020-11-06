"""
Daily Coding Problem: Problem #565 [Medium] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Pinterest.
Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.
For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
"""
def calc_hops(hops):
    i=hops[0]
    while(i<len(hops)):
        if hops[i] == 0:
            break
        i += hops[i]
    
    if i<len(hops)-1:
        return False
    else:
        return True

if __name__ == "__main__":
    print(calc_hops([2, 0, 1, 0]))
    print(calc_hops([1, 1, 0, 1]))
