#### Daily Coding Problem: Problem #104 [Easy] 
```
This problem was asked by Google.
Determine whether a doubly linked list is a palindrome. What if it’s singly linked?
For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False
```
[*code*](codesPython/coding104.py)

---
#### Daily Coding Problem: Problem #172 [Medium] 
```
This problem was asked by Dropbox.
Given a string s and a list of words words, where each word is the same length, 
find all starting indices of substrings in s that is a concatenation of 
every word in words exactly once. 

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], 
return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since
there are no substrings composed of "dog" and "cat" in s.
The order of the indices does not matter.
```
[*code*](codesPython/coding172.py)

---

#### Daily Coding Problem: Problem #173 [Easy] 
```
This problem was asked by Stripe.
Write a function to flatten a nested dictionary. Namespace the keys with a period.
For example, given the following dictionary:
{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:
{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur.
```
[*code*](codesPython/coding173.py)

---
#### Daily Coding Problem: Problem #178 [Hard]
```
This problem was asked by Two Sigma.
Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two simple probabilistic games.
The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. Your number of rolls is the amount you pay, in dollars.
The second game: same, except that the stopping condition is a five followed by a five.
Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the two games and calculate their expected value.
```
[*code*](codesPython/coding173.py)

---
#### Daily Coding Problem: Problem #185 [Easy]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.
For example, given the following rectangles:
{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
and
{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
return 6.
```
[*code*](codesPython/coding185.py)

---
#### Daily Coding Problem: Problem #399 [Hard]
```
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
```
[*code*](codesPython/coding399.py)

---
#### Daily Coding Problem: Problem #400 [Hard] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Goldman Sachs.
Given a list of numbers L, implement a method sum(i, j) which returns the sum from the sublist L[i:j] (including i, excluding j).
For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.
You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step.
```
[*code*](codesPython/coding399.py)

---
#### Daily Coding Problem: Problem #498 [Easy] 
```
This problem was asked by WhatsApp.
Given an array of integers out of order, determine the bounds of the smallest window that must be sorted in order for the entire array to be sorted. For example, given [3, 7, 5, 6, 9], you should return (1, 3).
```
[*code*](codesPython/coding498.py)

---
#### Daily Coding Problem: Problem #546 [Medium]
```
Daily Coding Problem: Problem #546 [Medium]
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.
For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:
•	There is 1 smaller element to the right of 3
•	There is 1 smaller element to the right of 4
•	There are 2 smaller elements to the right of 9
•	There is 1 smaller element to the right of 6
•	There are no smaller elements to the right of 1
```
[*code*](codesPython/coding546.py)

---
#### Daily Coding Problem: Problem #560 [Easy] 
```
Good morning! Here's your coding interview problem for today.
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
```
[*code*](codesPython/coding560.py)

---
#### Daily Coding Problem: Problem #562 [Hard]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
```
[*code*](codesPython/coding562.py)

---
#### Daily Coding Problem: Problem #565 [Medium] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Pinterest.
Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.
For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
```
[*code*](codesPython/coding565.py)

---
#### Daily Coding Problem: Problem #568 [Easy] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
Given a sorted list of integers, square the elements and give the output in sorted order.
For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
```
[*code*](codesPython/coding568.py)

---
#### Daily Coding Problem: Problem #649 [Easy] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
Given a string, return the first recurring character in it, or null if there is no recurring character.
For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
```
[*code*](codesPython/coding649.py)

---
#### Daily Coding Problem: Problem #650 [Hard] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
Let A be an N by M matrix in which every row and every column is sorted.
Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2].
For example, given the following matrix:
[[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]]

 And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 15 as there are 15 numbers in the matrix smaller than 6 or greater than 23.
```
[*code*](codesPython/coding650.py)

