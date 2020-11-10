"""
Daily Coding Problem: Problem #601 [Medium] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Pinterest.
The sequence [0, 1, ..., N] has been jumbled, and the only clue you have for its order is an array representing whether each number is larger or smaller than the last. Given this information, reconstruct an array that is consistent with it. For example, given [None, +, +, -, +], you could return [1, 2, 3, 0, 4].
"""

def recreate_array(array):
    numbers = []
    # found how many larger number in array would counter
    greater_num = sum([1 for  c in array if c =='+' ])
    #find first number 
    first = len(array)-greater_num-1
    numbers.append(first)
    
    small =  first-1
    large =  first+1

    for c in array[1:]:
        if c == '+':
            numbers.append(large)
            large+=1
        else:
            numbers.append(small)
            small+=1

    return numbers

if __name__ == "__main__":
    array = [None, '+', '+', '-', '+']
    print(recreate_array(array))


