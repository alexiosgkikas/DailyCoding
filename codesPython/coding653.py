"""
Daily Coding Problem: Problem #653 [Easy] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
You are given given a list of rectangles represented by min and max x- and y-coordinates. Compute whether or not a pair of rectangles overlap each other. If one rectangle completely covers another, it is considered overlapping.
For example, given the following rectangles:
{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}
return true as the first and third rectangle overlap each other.
"""

class Rectangle:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def doOverlap(self,rect):
        #check if one rect is on left side of other
        if self.x >= rect.x+rect.width or rect.x >= self.x+self.width:
            return False
        #check if one rect is above of other
        if self.y <= rect.y-rect.height or rect.y <= self.y-self.height:
            return False
        
        return True

    def __str__(self):
        return str(" Rectangle info: "+"left top:  ("+str(self.x)+","+str(self.y)+") , width: "+ str(self.width)+" , height: "+str(self.height))

def checkOverlap(ls):
    for i in range(0,len(ls)-1):
        for j in range(i+1,len(ls)):
            if ls[i].doOverlap(ls[j]):
                return True
    return False 

if __name__ == "__main__":
    ls = [
        Rectangle(1,4,3,3),
        Rectangle(-1,3,2,1),
        Rectangle(0,5,4,3)
    ]
    
    checkOverlap(ls)




