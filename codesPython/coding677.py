"""
Daily Coding Problem: Problem #677 [Easy]
Good morning! Here's your coding interview problem for today.
This problem was asked by Square.
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. The method is to take increasingly larger prime numbers, and mark their multiples as composite. 
For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. 
Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.
Implement this algorithm.
Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).
"""


def primes(N)->list():
    p =2 
    primes = [ True for i in range(0,N+1)]

    while(p*p < N+1):
        if primes[p] == True:
            for n in range(p*p,N+1,p):
                primes[n] = False
        p+=1
    
    s = [idx for idx,n in enumerate(primes) if n]
    return s[2:]

""" def primes(N) -> set():
    primes_num = set([2,3])
    for i in range(4,N+1):
        if all([i%p  for p in primes_num]):
            primes_num.add(i)
    
    return primes_num """

def main():
    print(primes(100))

if __name__ == "__main__":
    main()
