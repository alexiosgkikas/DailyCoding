# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 11:44:32 2019

@author: Alexios
"""



def overlap(r1,r2):
    #check if two rectangles are left  side from each other
    #first codition check if r1 is right side from r2
    #second codition check if r2 is right side from r1
    if r1[0] > (r2[0]+r2[2]) or r2[0] > (r1[0]+r1[2]):
        print("left side")
        return False
    #check if two rectangles are above each other
    if r1[1] < (r2[1]-r2[3]) or r2[1] < (r1[1]-r1[3]) :
        print("above side")
        return False
    return True

def findArea(r1,r2):
    
    if overlap(r1,r2):
        #find intersect width
        x = min((r1[0]+r1[2]),(r2[0]+r2[2])) - max (r1[0],r2[0])
        #find intersect height
        y = min(r1[1],r2[1]) - max(r1[1]-r1[3],r2[1]-r2[3])
        return x*y
    
    return 0

if __name__ == "__main__":
    r1=[1,4,3,3]
    r2=[0,5,4,3]
    print(findArea(r1,r2))