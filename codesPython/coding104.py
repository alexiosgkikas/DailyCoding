# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:38:53 2019

@author: Alexios
"""

#Daily Coding Problem: Problem #104 [Easy] 
class Node:
     def __init__(self,dataval=None,prev_Node =None, next_Node =None ):
        self.dataval = dataval
        self.prev_Node = prev_Node
        self.next_Node = next_Node

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addNode(self,dataval):
        if self.head is None:
            self.head = Node(dataval)
            self.tail = self.head
        else:
            self.tail.next_Node = Node(dataval,self.tail,None)
            self.tail =  self.tail.next_Node
    
    def printList(self):
        nd = self.head
        while nd.next_Node != None:
            print(nd.dataval,"->",end="")
            nd=nd.next_Node
        print(nd.dataval,"\n")
    
    
    def check_palindrome(self,head,tail):
        if head is tail:
            return True
        if head.dataval is tail.dataval:
            if head.next_Node is tail.prev_Node:
                return True
            else:
                return self.check_palindrome(head.next_Node,tail.prev_Node)
        else:
            return False
        
    
if __name__ == "__main__":
    dl  = DLinkedList()
    dl.addNode(1)
    dl.addNode(2)
    dl.addNode(3)
    dl.addNode(4)
    dl.addNode(4)
    dl.addNode(3)
    dl.addNode(2)
    dl.addNode(1)
    
    dl.printList()
    print(dl.check_palindrome(dl.head,dl.tail))