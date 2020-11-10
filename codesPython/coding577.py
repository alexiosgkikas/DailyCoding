"""
Daily Coding Problem: Problem #577 [Medium]
Good morning! Here's your coding interview problem for today.
This problem was asked by Dropbox.
Given a list of words, determine whether the words can be chained to form a circle. A word X can be placed in front of another word Y in a circle if the last character of X is same as the first character of Y.
For example, the words ['chair', 'height', 'racket', touch', 'tunic'] can form the following circle: chair --> racket --> touch --> height --> tunic --> chair.
"""
"""
SOLUTION 1
"""
def chain(words,prev_word,word_list):
    word_list.append(prev_word)# add previous word
    words.remove(prev_word) # remove word from not used words, to avoid looping between words
    if len(words)==0 and word_list[0][0] ==  word_list[-1][-1] : 
        #print("found: ",word_list)
        return True
    _next = []
    for word in words:
        if word not in word_list and word[0] == word_list[-1][-1] :
            _next.append(chain(words.copy(),word,word_list.copy()))    
    if len(_next) == 0:
        return False
    else:
        return any([ t for t in _next])

def IsChain(words):
    for word in words:
        word_list = []
        # we need to copy so it would not overwrite betwwen recursions
        if chain(words.copy(),word,word_list.copy()):
            #print("chain with starting word: ",word)
            return True
    return False
"""
SOLUTION 2 with Tree Node
"""
class Node:
    def __init__(self,word,words_left):
        self.word = word
        self.words_left = words_left
        self.words_left.remove(self.word)
        self.childs = [Node(w,self.words_left.copy()) for w in self.words_left if  w[0] == self.word[-1]]

    def printTree(self):
        if len(self.childs) == 0:
            print("Parent: ",self.word," with no childs")
        else:
            print("Parent: ",self.word," with childs: ")
            for c in self.childs:
                c.printTree()

def findMaxDepth(root):
    if root.word is None or len(root.childs)==0:
        return 1
    
    return max([findMaxDepth(child) for child in root.childs])+1

def isChainNode(words):
    for word in words:
        root = Node(word,words.copy())
        if findMaxDepth(root) == len(words):
            #print("There is chain in words starting with ",root.word)
            return True
    return False

if __name__ == "__main__":
    words  = ['chair', 'height', 'racket', 'touch', 'tunic']
    print(IsChain(words))
    words  = ['abb', 'bbasa']
    print(IsChain(words))
    words  = ['height', 'racket','touch']
    print(IsChain(words))
    #Solution 2 with tree
    words  = ['chair', 'height', 'racket', 'touch', 'tunic']
    print(isChainNode(words))
