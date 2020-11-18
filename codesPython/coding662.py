"""
Daily Coding Problem: Problem #662 [Easy]
Good morning! Here's your coding interview problem for today.
This problem was asked by Amazon.
Given n numbers, find the greatest common denominator between them.
For example, given the numbers [42, 56, 14], return 14.
"""

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def max_com_den(numbers):
    g = gcd(numbers[0],numbers[1])
    for n in numbers[2:]:
        g = gcd(g,n)
    
    return g

if __name__ == "__main__":
    numbers = [42, 56, 14]
    print(max_com_den(numbers))