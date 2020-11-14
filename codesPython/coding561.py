"""
Daily Coding Problem: Problem #561 [Hard] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Etsy.
Given a sorted array, convert it into a height-balanced binary search tree.
"""
import math

class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

    def preOrder(self):
        if self.left:
            self.left.preOrder()
        print(self.value)
        if self.right:
            self.right.preOrder()

def createTree(root,array):
    if len(array) == 0: 
        return None
    root = Node(array[ int(len(array)/2) ])
    root.left = createTree(root.left, array[0:int(len(array)/2)])
    root.right = createTree(root.right, array[int(len(array)/2)+1:])
    return root

def height(root):
    if root == None:
        return 0
    return max(height(root.left),height(root.right))+1


if __name__ == '__main__':
    array  = [1,2,3,4,5,6,7,8,9,10,11,12]
    root  = None
    root = createTree(root,array)
    root.preOrder()
