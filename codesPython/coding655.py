"""
Daily Coding Problem: Problem #655 [Easy] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Facebook.
Given a 32-bit integer, return the number with its bits reversed.
For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, return 0000 1111 0000 1111 0000 1111 0000 1111.
"""


def reverseBits(bits) :       
    reversed=""
    for bit in bits:
        reversed+=str((int(bit)+1)%2)
    return reversed
    # with one line 
    #return "".join([(int(bit)+1)%2 for bit in bits ]


if __name__ == "__main__":
    num = "11110000111100001111000011110000"
    print(reverseBits(num))

