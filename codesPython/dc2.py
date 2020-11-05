"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
You are given a starting state start, a list of transition probabilities for a Markov chain, and a number of steps num_steps. Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.
For example, given the starting state a, number of steps 5000, and the following transition probabilities:
[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
"""
import random

visited = {'a': 0, 'b': 0, 'c': 0 }
markov = {'a': ( ('a', 0.9),  ('b', 0.075), ('c', 0.025)),
          'b': ( ('a', 0.15), ('b', 0.8),   ('c', 0.05) ),
          'c': ( ('a', 0.25), ('b', 0.25),  ('c', 0.05) )
        }

def steps(start,num_steps):
    if num_steps == 0:
        return 0
    #add 1 for visiting 
    for i in range(0,num_steps):
        visited[start] = visited[start] + 1
        #get tuple list for given start state
        get_prob = markov[start]
        # using list comprehension for listing states and probabilities
        states = [t[0] for t in get_prob]
        probs = [t[1] for t in get_prob]
        #get next state 
        start = random.choices(states,weights=probs,k=1)[0]

if __name__ == "__main__":
    steps('a',15000)
    print(visited)
