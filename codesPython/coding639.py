"""
Daily Coding Problem: Problem #639 [Easy] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Yelp.
Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.
For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
"""

def create_pairs(l1=None,l2=None):
    if l1 == None:
        return l2
    if l2 ==None:
        return l1

    list_pairs = []
    for i in range(0,len(l1)):
        for j in range(0,len(l2)):
            list_pairs.append(l1[i]+l2[j])
    return list_pairs


def create_all_possibly_pairs(dictionary,num):
    poss = None
    while num!=0:
        poss=create_pairs(dictionary[num%10],poss)
        num = int(num/10)
    return poss




if __name__ == "__main__":
    dictionary = {
        2:['a','b','c'],
        3:['d','e','f'],
        4:['g','h','i'],
        5:['j','k','l'],
        6:['m','n','o'],
        7:['p','q','r','s'],
        8:['t','u','v'],
        9:['w','x','y','z']
    }
    
    print(create_all_possibly_pairs(dictionary,234))
