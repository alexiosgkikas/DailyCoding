"""
Daily Coding Problem: Problem #642 [Easy]
Good morning! Here's your coding interview problem for today.
This problem was asked by Pivotal.
A step word is formed by taking a given word, adding a letter, and anagramming the result. For example, starting with the word "APPLE", you can add an "A" and anagram to get "APPEAL".
Given a dictionary of words and an input word, create a function that returns all valid step words.
"""

def step_words(dictionary,word):
    sw = set()
    ws = set(list(word))
    print(ws)
    for dw in dictionary:
        if len(dw)-1 == len(word):
            temp = dw
            for  c in ws:
                dw = dw.replace(c,'')
            if len(dw) ==1 or len(dw) ==0:
                sw.add(temp)
                
    return sw if len(sw) > 0 else None


if __name__ == "__main__":
    dictionary = [
        "APPLE",
        "APPEAL",
        "WORD",
        "WORKSHOP",
        "HAPPLE",
        "ALPES"
    ]
    print(step_words(dictionary,"ASASA"))
    print(dictionary)


