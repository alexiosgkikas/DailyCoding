"""
Daily Coding Problem: Problem #678 [Easy] 
Good morning! Here's your coding interview problem for today.
This problem was asked by IBM.
Given an integer, find the next permutation of it in absolute order. For example, given 48975, the next permutation would be 49578.
"""


def next_premutation(number) -> int:
    pivot = len(number)-1
    # find longest non-increasing suffix  
    for i in  range(pivot-1,0,-1):
        if number[i]>= number[i+1]:
            pivot = i
        else:
            break
    #set pivot
    pivot-=1
    # find the righmost successor to pivot in the suffix 
    for i in range(len(number)-1,pivot,-1):
        if number[i]>number[pivot]:
            p = number[pivot]
            number[pivot] = number[i]
            number[i] = p
            break
    
    #reverse suffix
    number = number[0:pivot+1]+number[len(number):pivot:-1]
    return number


def main():
    print(next_premutation([4,8,9,7,5]))
    print(next_premutation([4,9,9,9,9]))

if __name__ == "__main__":
    main()
