"""
Daily Coding Problem: Problem #682 [Medium] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Squarespace.
Write a function, add_subtract, which alternately adds and subtracts curried arguments. Here are some sample operations:
add_subtract(7) -> 7

add_subtract(1)(2)(3) -> 1 + 2 - 3 -> 0

add_subtract(-5)(10)(3)(9) -> -5 + 10 - 3 + 9 -> 11
"""
def sum_args(*args):
    return sum([ x if idx%2==1 or idx==0 else -x for idx,x in enumerate(args)])

def curry(func):
    f_args = []
    def f(*args):
        nonlocal f_args
        if args :
            f_args+=args
            return f
        else:#situation when reach an empty curly to when to stop
            print(f_args)
            result = func(*f_args)
            f_args = []
            return result       
    return f

add_subtract = curry(sum_args)
print(add_subtract(7)())
print(add_subtract(1)(2)(3)())
print(add_subtract(-5)(10)(3)(9)())

