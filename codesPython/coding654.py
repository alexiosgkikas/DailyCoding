"""
Daily Coding Problem: Problem #654 [Medium]
Good morning! Here's your coding interview problem for today.
This problem was asked by Amazon.
Given a string, find the length of the smallest window that contains every distinct character. Characters may appear more than once in the window.
For example, given "jiujitsu", you should return 5, corresponding to the final five letters.
"""

def distinct_window(word):
    #first check from left to right and then from right to left
    left1  = 0
    right1 = len(word)-1   
    while(word[left1] in word[left1+1:]):
        left1+=1
    while(word[right1] in word[left1:right1-1]):
        right1-=1
    
    #second check from right to left and then left to right
    left2  = 0
    right2 = len(word)-1    
    while((word[right2] in word[:right2-1])):
        right2-=1
    while(word[left2] in word[left2+1:right2+1]):
        left2+=1

    print("Word from left to right: "+word[left1:right1+1]+" size: "+str(len(word[left1:right1+1])))
    print("Word from right to left: "+ word[left2:right2+1]+" size: "+str(len(word[left2:right2+1])))

    return  min(right1-left1+1,right2-left2+1)

if __name__ == "__main__":
    word = "jiujitsu"
    print(distinct_window(word))
    word = "jitsujiu"
    print(distinct_window(word))
    word = "alohaalohallbalohaaloha"
    print(distinct_window(word))
