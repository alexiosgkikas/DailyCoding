"""
Daily Coding Problem: Problem #575 [Medium] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Uber.
Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:
•	next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
•	has_next(): returns whether or not the iterator still has elements left.
For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.
Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
"""
class Iterator2D:
    def __init__(self, arraylist):
        self.arraylist = arraylist
        self.indexlist = 0
        self.iterator = -1

    def next(self):
        try:
            self.has_next()
            self.iterator+=1
            return self.arraylist[self.indexlist][self.iterator]
        except: 
            raise LookupError("Iterator Error. No more items in list!!!!!")
    

    def has_next(self):
        try:
            #check if cuurent sub-array has next item
            self.arraylist[self.indexlist][self.iterator+1]
            return True
        except IndexError:
            try:
                # if current sub-array doesnt have next item ,
                # check if next sub-array exits
                # and if exist point to next sub-array and change index of item 
                self.arraylist[self.indexlist+1] 
                self.indexlist +=1
                self.iterator = -1
                return self.has_next()
            except IndexError:
                #raise when there is no other sub-array 
                return False

if __name__ == "__main__":

    arraylists = [
        [1,2],
        [3],
        [],
        [4,5,6]
    ]

    d2 = Iterator2D(arraylists)
    print(d2.next())
    print(d2.next())
    print(d2.next())
    print(d2.next())
    print(d2.next())
    print(d2.next())
    print("==============================================")
    d2 = Iterator2D([[],[1]])
    print(d2.next())