"""
Daily Coding Problem: Problem #578 [Easy] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Bloomberg.
Determine whether there exists a one-to-one character mapping from one string s1 to another s2.
For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.
Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
"""
def doMap(str1,str2):
    if len(str1) != len(str2):
        return False
    map_dict =dict()  
    index =0
    while(index<len(str1)):
        if str1[index] in map_dict:
            if map_dict[str1[index]] != str2[index]:
                return False
        else:
            map_dict[str1[index]] =  str2[index]
        
        index+=1
    return True

if __name__ == "__main__":
    print(doMap("abc","bcd"))
    print(doMap("foo","bar"))

