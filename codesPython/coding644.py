"""
Daily Coding Problem: Problem #644 [Easy] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

class Node:

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.value)
        if self.right:
            self.right.PrintTree()


def isUnival(root):
    if root is None:
        return True
    
    if root.left:
        if root.left.value != root.value:
           return False
    if root.right:
        if root.right.value != root.value:
           return False 
    
    if  isUnival(root.left) and isUnival(root.right):
        return True

    return False

def countUnival(root):
    if root is None:
        return 0
    count_left= countUnival(root.left)
    count_right= countUnival(root.right)
    if isUnival(root):
        return 1+count_left+count_right
    else:
        return count_left+count_right



        

if __name__ == "__main__":
    root1= Node(0)
    root1.left = Node(1)
    root1.right = Node(0)
    root1.right.left = Node(1)
    root1.right.right = Node(0)
    root1.right.left.left = Node(1)
    root1.right.left.right = Node(1)
    #root1.PrintTree()
    print("count: ",countUnival(root1))



