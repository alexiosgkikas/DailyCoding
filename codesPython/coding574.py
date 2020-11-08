"""
Daily Coding Problem: Problem #574 [Medium] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Amazon.
Implement a bit array.
A bit array is a space efficient array that holds a value of 1 or 0 at each index.
•	init(size): initialize the array with size
•	set(i, val): updates index at i with val where val is either 1 or 0.
•	get(i): gets the value at index i.
"""

class BitArray:
    def __init__(self, size):
        if size<=0:
            raise LookupError("Array cannot have negative size")
        self.size = size
        self.array = [0]*size

    def set(self,i,val):
        if i>=self.size:
            raise LookupError("Index out of bound")
        
        if val is not 0 or not 1:
            raise LookupError("Ivalid value. Only 1s and 0s")

        self.array[i] = val
    
    def get(self,i):
        return self.array[i]

if __name__ == "__main__":

    bit = BitArray(10)
    print(bit.array)
    bit.set(3,1)
    print(bit.array)
    bit.set(6, 1)
    bit.set(8, 1)
    bit.set(3, 0) 
    print(bit.array)
    bit.set(10, 1)  



