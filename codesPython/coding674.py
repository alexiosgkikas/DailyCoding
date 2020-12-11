"""
Daily Coding Problem: Problem #674 [Easy]
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
A girl is walking along an apple orchard with a bag in each hand. She likes to pick apples from each tree as she goes along, but is meticulous about not putting different kinds of apples in the same bag.
Given an input describing the types of apples she will pass on her path, in order, determine the length of the longest portion of her path that consists of just two types of apple trees.
For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, with a length of four.
"""

def max_portion(apples):
    maxi= 0

    for i in range(0,len(apples)-1):
        if maxi > len(apples)-i:
            break
        ls = set([apples[i]])
        for j in range(i+1,len(apples)):
            ls.add(apples[j])
            if len(ls) > 2:
                maxi  = max(maxi,j-i)
                break
    
    return maxi            
                 

def main():
    apples = [2, 1, 2, 3, 3, 1, 3, 5]
    print(max_portion(apples))

if __name__ == "__main__":
    main()