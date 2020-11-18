"""
Daily Coding Problem: Problem #651 [Medium] 
Good morning! Here's your coding interview problem for today.
This problem was asked by LinkedIn.
Determine whether a tree is a valid binary search tree.
A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self,value):
        if self.value == None:
            self.value = value
        else:
            if self.value >= value:
                if self.left is None:
                    self.left = Node(value)
                else:
                     self.left.insert(value)
            elif self.value < value:
                if self.right is None:
                    self.right = Node(value)
                else:
                     self.right.insert(value)

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.value)
        if self.right:
            self.right.printTree()

INT_MAX = 4294967296
INT_MIN = -4294967296

def checkvalidation(root,mini,maxi):
    if root is  None: 
        return True
    if (root.value<mini or root.value >maxi):
        return False
    return (checkvalidation(root.left,mini,root.value-1)
             and  checkvalidation(root.right,root.value+1,maxi))


if __name__ == "__main__":
    root = Node(12)
    root.insert(10)
    root.insert(13)
    root.insert(14)
    root.printTree()
    
    print(checkvalidation(root,INT_MIN,INT_MAX))