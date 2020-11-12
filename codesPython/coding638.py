"""
Daily Coding Problem: Problem #638 [Medium] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"
Follow-up: given a mutable string representation, can you perform this operation in-place?
"""
#with one line (python style)
def reverse1(str1):
    return " ".join(str1.split(" ")[::-1])

#with recursion
def reverse2(str1):
    if len(str1)<0:
        return ''
    left = 0
    for ch in str1:
        if ch != " " and left<len(str1):
            left+=1
        else:
            break
    if left<len(str1):
        return reverse2(str1[left+1:])+' '+str1[0:left]
    else:
        return str1


if __name__ == "__main__":
    str1 = "hello world here"
    str2 = reverse1(str1)
    print(str2)
    assert len(str1) == len(str2)