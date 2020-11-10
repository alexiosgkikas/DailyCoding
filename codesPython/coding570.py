"""
Daily Coding Problem: Problem #570 [Hard] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
"""

class Node:

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self,value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)

        else:
            self.value = value

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.value),
        if self.right:
            self.right.PrintTree()

def checkSubTree(root1,root2):
    if root1 is None and root2 is None:
        return True

    if (root1 is None or root2 is None)  or (root1.value != root2.value):
        return False
    else:
        return (checkSubTree(root1.left,root2.left) and checkSubTree(root1.right,root2.right))

if __name__ == "__main__":
    print("Tree 1 ")
    root1= Node(10)
    root1.insert(5)
    root1.insert(12)
    root1.insert(15)
    print("Tree 2 ")
    root2= Node(10)
    root2.insert(5)
    root2.insert(12)
    root2.insert(15)
    print("Checking Tree1 with Tree2:  "+ str(checkSubTree(root1,root2)))
    root2.insert(7)
    print("Checking Tree1 with Tree2 after insert:  "+  str(checkSubTree(root1,root2)))















