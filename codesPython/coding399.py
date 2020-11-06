"""
Daily Coding Problem: Problem #399 [Hard] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Facebook.
Given a list of strictly positive integers, partition the list into 3 contiguous partitions which each sum up to the same value. If not possible, return null.
For example, given the following list:
[3, 5, 8, 0, 8]
Return the following 3 partitions:
[[3, 5],
 [8, 0],
 [8]]
Which each add up to 8.
"""

def split_array(array):
    
    if sum(array)%3 !=0 or max(array)>sum(array)%3:
        return None
    
    max_sum =(int) (sum(array)/3)
    ls = []

    while(len(array)>0):
        temp = [array[0]]
        array.pop(0)
        index = 0
        while(sum(temp)<8):
            if (sum(temp)+array[index]) <= max_sum:
                temp.append(array[index])
                array.pop(index)
            else:
                index += 1
        ls.append(temp)
    return ls



if __name__ == "__main__":
    array = [3, 5, 8, 0, 8]
    print(split_array(array))