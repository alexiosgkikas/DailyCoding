"""
Daily Coding Problem: Problem #676 [Hard]
Good morning! Here's your coding interview problem for today.
This problem was asked by LinkedIn.
Given a string, return whether it represents a number. Here are the different kinds of numbers:
•	"10", a positive integer
•	"-10", a negative integer
•	"10.1", a positive real number
•	"-10.1", a negative real number
•	"1e5", a number in scientific notation
And here are examples of non-numbers:
•	"a"
•	"x 1"
•	"a -2"
•	"-"
"""



def isValidNumber(number):
    number = number.lstrip().rstrip()
    if len(number) == 0:
        return False


    if len(number) == 1:
        if number[0] not in "0123456789":
            return False
        else:
            return True

    # [+,-,.,0..9,e]
    
    symbol = False

    for i in range(0,len(number)):
        print(number[i])

        #check if 
        if number[i] not in "0123456789e.+-":
            print("break1")
            return False

        if (number[i] == '-' or number[i] == '+') and i !=0:
            return False
        
        if  (number [i] == 'e' or number [i] == '.') and (i ==0 or i == len(number) -1 or symbol == True):
            return False
        
        if number [i] == 'e' or number [i] == '.':
            symbol= True

    return True



if __name__=="__main__":
    print(isValidNumber("2.2.2"))