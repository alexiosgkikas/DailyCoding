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
#### Daily Coding Problem: Problem #570 [Hard] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
```
[*code*](codesPython/coding570.py)

---
#### Daily Coding Problem: Problem #574 [Medium] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Amazon.
Implement a bit array.
A bit array is a space efficient array that holds a value of 1 or 0 at each index.
•	init(size): initialize the array with size
•	set(i, val): updates index at i with val where val is either 1 or 0.
•	get(i): gets the value at index i.
```
[*code*](codesPython/coding574.py)

---
#### Daily Coding Problem: Problem #575 [Medium] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Uber.
Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:
•	next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
•	has_next(): returns whether or not the iterator still has elements left.
For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.
Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
```
[*code*](codesPython/coding575.py)

---
#### Daily Coding Problem: Problem #577 [Medium]
```

Good morning! Here's your coding interview problem for today.
This problem was asked by Dropbox.
Given a list of words, determine whether the words can be chained to form a circle. A word X can be placed in front of another word Y in a circle if the last character of X is same as the first character of Y.
For example, the words ['chair', 'height', 'racket', touch', 'tunic'] can form the following circle: chair --> racket --> touch --> height --> tunic --> chair.
```
[*code*](codesPython/coding577.py)

---
#### Daily Coding Problem: Problem #599 [Hard]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Two Sigma.
Ghost is a two-person word game where players alternate appending letters to a word. The first person who spells out a word, or creates a prefix for which there is no possible continuation, loses. Here is a sample game:
•	Player 1: g
•	Player 2: h
•	Player 1: o
•	Player 2: s
•	Player 1: t [loses]
Given a dictionary of words, determine the letters the first player should start with, such that with optimal play they cannot lose.
For example, if the dictionary is ["cat", "calf", "dog", "bear"], the only winning start letter would be b.
```
[*code*](codesPython/coding599.py)

---
#### Daily Coding Problem: Problem #600 [Easy] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
Given a set of points (x, y) on a 2D cartesian plane, find the two closest points. For example, given the points [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)], return [(-1, -1), (1, 1)].
```
[*code*](codesPython/coding600.py)

---
#### Daily Coding Problem: Problem #601 [Medium] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Pinterest.
The sequence [0, 1, ..., N] has been jumbled, and the only clue you have for its order is an array representing whether each number is larger or smaller than the last. Given this information, reconstruct an array that is consistent with it. For example, given [None, +, +, -, +], you could return [1, 2, 3, 0, 4].
```
[*code*](codesPython/coding601.py)

---
#### Daily Coding Problem: Problem #638 [Medium]
```

Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"
Follow-up: given a mutable string representation, can you perform this operation in-place?
```
[*code*](codesPython/coding638.py)

---
#### Daily Coding Problem: Problem #639 [Easy] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Yelp.
Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.
For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
```
[*code*](codesPython/coding639.py)

---
#### Daily Coding Problem: Problem #641 [Easy] 
```
This problem was asked by Amazon.
Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.
For example, for the input [1, 2, 3, 10], you should return 7.
Do this in O(N) time.
```
[*code*](codesPython/coding641.py)

---
#### Daily Coding Problem: Problem #644 [Easy] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
```
[*code*](codesPython/coding644.py)

---
#### Daily Coding Problem: Problem #645 [Easy]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Microsoft.
Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.
For example, given the following matrix:
[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.
```
[*code*](codesPython/coding645.py)

---
#### Daily Coding Problem: Problem #647 [Medium] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Facebook.
Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.
For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.
Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum
```
[*code*](codesPython/coding647.py)

---
#### Daily Coding Problem: Problem #648 [Medium]
```
Good morning! Here's your coding interview problem for today.
This question was asked by Snapchat.
Given the head to a singly linked list, where each node also has a “random” pointer that points to anywhere in the linked list, deep clone the list.
```
[*code*](codesPython/coding648.py)

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

---
#### Daily Coding Problem: Problem #653 [Easy] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
You are given given a list of rectangles represented by min and max x- and y-coordinates. Compute whether or not a pair of rectangles overlap each other. If one rectangle completely covers another, it is considered overlapping.
For example, given the following rectangles:
{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}
return true as the first and third rectangle overlap each other.
```
[*code*](codesPython/coding653.py)

---
#### Daily Coding Problem: Problem #654 [Medium]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Amazon.
Given a string, find the length of the smallest window that contains every distinct character. Characters may appear more than once in the window.
For example, given "jiujitsu", you should return 5, corresponding to the final five letters.
```
[*code*](codesPython/coding654.py)

---
#### Daily Coding Problem: Problem #655 [Easy] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Facebook.
Given a 32-bit integer, return the number with its bits reversed.
For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, return 0000 1111 0000 1111 0000 1111 0000 1111.
```
[*code*](codesPython/coding655.py)

---
#### Daily Coding Problem: Problem #656 [Medium] 
```
Good morning! Here's your coding interview problem for today.
Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.
For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:
B B W
W W W
W W W
B B B
Becomes
B B G
G G G
G G G
B B B
```
[*code*](codesPython/coding656.py)

---
#### Daily Coding Problem: Problem #657 [Easy] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
You may also use a list or array to represent a set.
```
[*code*](codesPython/coding657.py)

---