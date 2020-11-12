"""
Daily Coding Problem: Problem #580 [Easy] 
Good morning! Here's your coding interview problem for today.
This question was asked by Apple.
Given a binary tree, find a minimum path sum from root to a leaf.
For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.
  10
 /  \
5    5
 \     \
   2    1
       /
     -1
"""

import sys

class Node:
    def __init__(self,value,left = None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def printTree(self):
        if self.value:
            print(self.value)
            if self.left:
                self.left.printTree()
            if self.right: 
                self.right.printTree()


def minimumSumPath(node):
    if node == None:
        return [sys.maxsize]
    
    print("Node value: ",node.value)
    if node.value and (node.left == None and node.right == None):
        print("returning leaf: ",node.value)
        return [node.value]
    
    left =[]
    right =[]
    left += minimumSumPath(node.left)
    right += minimumSumPath(node.right)
    print(left,right)

    if sum(left)<sum(right):
        return [node.value]+left
    else:
        return [node.value]+right
    

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.left.right = Node(2)
    root.right = Node(5)
    root.right.right = Node(1)
    root.right.right.left = Node(-1)
    
    print(minimumSumPath(root))

    
