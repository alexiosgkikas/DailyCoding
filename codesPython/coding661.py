"""
Daily Coding Problem: Problem #661 [Hard]
Good morning! Here's your coding interview problem for today.
This problem was asked by Netflix.
Given a sorted list of integers of length N, determine if an element x is in the list without performing any multiplication, division, or bit-shift operations.
Do this in O(log N) time.
"""
#code from https://www.geeksforgeeks.org/fibonacci-search/
# Python3 program for Fibonacci search. 
from bisect import bisect_left 
  
# Returns index of x if present,  else  
# returns -1  
def fibMonaccianSearch(arr, x): 
      
    # Initialize fibonacci numbers  
    fibMMm2 = 0 # (m-2)'th Fibonacci No. 
    fibMMm1 = 1 # (m-1)'th Fibonacci No. 
    fibM = fibMMm2 + fibMMm1 # m'th Fibonacci 
  
    # fibM is going to store the smallest  
    # Fibonacci Number greater than or equal to n  
    while (fibM < len(arr)): 
        fibMMm2 = fibMMm1 
        fibMMm1 = fibM 
        fibM = fibMMm2 + fibMMm1 
    print(len(arr))
    print(fibMMm2,fibMMm1,fibM)
    # Marks the eliminated range from front 
    offset = -1; 
  
    # while there are elements to be inspected. 
    # Note that we compare arr[fibMm2] with x. 
    # When fibM becomes 1, fibMm2 becomes 0  
    while (fibM > 1): 
          
        # Check if fibMm2 is a valid location 
        i = min(offset+fibMMm2, len(arr)-1) 
        print("======================================")
        print("checking with  fibM {} ,fibMMm1 {} ,fibMMm2 {} , offset {} ,poistion {}".format(fibM,fibMMm1,fibMMm2,offset,i))
        print("arr[i],x: ",arr[i],x)
        # If x is greater than the value at  
        # index fibMm2, cut the subarray array  
        # from offset to i  
        if (arr[i] < x): 
            fibM = fibMMm1 
            fibMMm1 = fibMMm2 
            fibMMm2 = fibM - fibMMm1 
            offset = i
            print("IS GREATER fibM {} ,fibMMm1 {} ,fibMMm2 {} ,offset {}".format(fibM,fibMMm1,fibMMm2,offset))

        # If x is less than the value at  
        # index fibMm2, cut the subarray  
        # after i+1 
        elif (arr[i] > x): 
            fibM = fibMMm2 
            fibMMm1 = fibMMm1 - fibMMm2 
            fibMMm2 = fibM - fibMMm1 
            print("IS LESS fibM {} ,fibMMm1 {} ,fibMMm2 {} ,offset {}".format(fibM,fibMMm1,fibMMm2,offset))

        # element found. return index  
        else : 
            return i 
  
    # comparing the last element with x */ 
    if(fibMMm1 and arr[offset+1] == x): 
        return offset+1; 
  
    # element not found. return None  
    return None


if __name__ == "__main__":
    ls = [1,2,3,4,5,6,7,8,9,10,11,12]
    #print(exist(ls,3))
    
    print(fibMonaccianSearch(ls,-1))