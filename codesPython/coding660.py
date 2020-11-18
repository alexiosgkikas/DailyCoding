"""
Daily Coding Problem: Problem #660 [Hard] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Airbnb.
You come across a dictionary of sorted words in a language you've never seen before. Write a program that returns the correct order of letters in this language.
For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], you should return ['x', 'z', 'w', 'y'].
"""
# code from https://medium.com/@dimko1/alien-dictionary-6cf2da24bf3c

import collections

def letters_order(words):
    pre = collections.defaultdict(set)
    suc = collections.defaultdict(set)
    
    for pair in zip(words, words[1:]):
        for a, b in zip(*pair):
            #print(zip(*pair))
            if a != b:
                suc[a].add(b)
                pre[b].add(a)
                break
    print("pre",pre)
    print("suc",suc)
    chars = set(''.join(words))
    charToProcess = chars - set(pre)
    order = ''
    print("charToProcess: ",charToProcess)
    while charToProcess:
        ch = charToProcess.pop()
        order += ch
        for b in suc[ch]:
            pre[b].discard(ch)
            if not pre[b]:
                charToProcess.add(b)
    
    return list(order) * (set(order) == chars)

if __name__ == "__main__":
    words = ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']
    print(letters_order(words))