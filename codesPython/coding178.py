# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:47:11 2019

@author: Alexios
"""

from random import randint


def roll_dice(num_rolls,states_end):
    states = [0,0]
    count = 0
    i = 0
    for i in range(0,num_rolls):
        dice = randint(1,6)
        count+=1
        current = i%len(states)
        previous = (i+1)%len(states)# len(states)-(current-1) 
        states[current] =dice
        print("current state ", states[current])
        if states[previous] == states_end[0] and states[current] == states_end[1]:
            return count
        
    return count
        

if __name__ == "__main__":
    num_rolls = 1000
    
    states_end =[5,6]
    
    print(roll_dice(100,states_end))