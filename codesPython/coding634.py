"""
Daily Coding Problem: Problem #634 [Medium]
Good morning! Here's your coding interview problem for today.
This problem was asked by Square.
You are given a histogram consisting of rectangles of different heights. These heights are represented in an input list, such that [1, 3, 2, 5] corresponds to the following diagram:
      x
      x  
  x   x
  x x x
x x x x
Determine the area of the largest rectangle that can be formed only from the bars of the histogram. For the diagram above, for example, this would be six, representing the 2 x 3 area at the bottom right.
"""
def max_area(histogram):
    
    height = 0
    width = 0
    max_area = 0
    for i in range(0,len(histogram)):
        # check form left 
        left = i
        for j in range(left-1,-1,-1):
            if histogram[i]<=histogram[j]:
                left-=1
            else:
                break
        # check from right
        right = i
        for j in range(right+1,len(histogram)):
            if histogram[i]<=histogram[j]:
                right+=1
            else:
                break
        max_area = max(max_area, histogram[i]*(right-left+1) )

    return max_area

if __name__ == "__main__":
    histogram =  [1, 3, 2, 5]
    print(max_area(histogram))



