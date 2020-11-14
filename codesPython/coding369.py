"""
Daily Coding Problem: Problem #599 [Hard] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Two Sigma.
Ghost is a two-person word game where players alternate appending letters to a word. The first person who spells out a word, or creates a prefix for which there is no possible continuation, loses. Here is a sample game:
•	Player 1: g
•	Player 2: h
•	Player 1: o
•	Player 2: s
•	Player 1: t [loses]
Given a dictionary of words, determine the letters the first player should start with, such that with optimal play they cannot lose.
For example, if the dictionary is ["cat", "calf", "dog", "bear"], the only winning start letter would be b.
"""

def start_letters(dictionary):
    charset = dict()
    for word in dictionary:
        if word[0] not in charset:
            charset[word[0]] = []
        charset[word[0]].append(len(word))

    possibly_start = []
    for char in charset:
        if all([len_word%2==0 for len_word in charset[char]]):
            possibly_start.append(char)
        #if you want based on possibility
        # count = 0  
        # for len_word in charset[char]:
        #     if int(len_word%2) == 0 :
        #         count+=1
        #     possibly_start.append((char,count/len(charset[char])))

    return possibly_start

if __name__ == "__main__":
    dictionary = ["cat", "calf", "dog", "bear"]
    print(start_letters(dictionary))