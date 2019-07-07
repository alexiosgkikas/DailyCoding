# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 18:47:30 2019

@author: Alexios
"""




def find_word(s,words):
    if not  words:
        #print("found full word")
        return True
    w= words[0]
    if w in s:
        #print("found word: "+w+ " in "+s)
        s= s.replace(w,'')
        return find_word(s,words[1:])
    else:
        return False
    

if __name__ == "__main__":
    list_indices = []
    s = "dogcatcatcodecatdog"
    words = ["dog","cat"]
    maxsize_word = len(words)*len(words[0])
    for i in range(0,len(s)-maxsize_word+1):
        print(s[i:i+maxsize_word])
        if find_word(s[i:i+maxsize_word],words) :
            list_indices.append(i)
    
    print(list_indices)
    