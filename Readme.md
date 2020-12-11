#### Daily Coding Problem: Problem #2 [Hard]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
```
[*code*](codesPython/coding2.py)

---
#### Daily Coding Problem: Problem #17 [Hard] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.
```
[*code*](codesPython/coding658.py)

---
#### Daily Coding Problem: Problem #98 [Easy]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Coursera.
Given a 2D board of characters and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
For example, given the following board:
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
```
[*code*](codesPython/coding98.py)

---
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
#### Daily Coding Problem: Problem #296 [Hard]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Etsy.
Given a sorted array, convert it into a height-balanced binary search tree.
```
[*code*](codesPython/coding296.py)

---
#### Daily Coding Problem: Problem #309 [Hard] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Grammarly.
Soundex is an algorithm used to categorize phonetically, such that two names that sound alike but are spelled differently have the same representation.
Soundex maps every name to a string consisting of one letter and three numbers, like M460.
One version of the algorithm is as follows:
1.	Remove consecutive consonants with the same sound (for example, change ck -> c).
2.	Keep the first letter. The remaining steps only apply to the rest of the string.
3.	Remove all vowels, including y, w, and h.
4.	Replace all consonants with the following digits:
o	b, f, p, v → 1
o	c, g, j, k, q, s, x, z → 2
o	d, t → 3
o	l → 4
o	m, n → 5
o	r → 6
5.	If you don't have three numbers yet, append zeros until you do. Keep the first three numbers.
Using this scheme, Jackson and Jaxen both map to J250.
Implement Soundex.
```
[*code*](codesPython/coding604.py)

---
#### Daily Coding Problem: Problem #369 [Hard]
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
[*code*](codesPython/coding369.py)

---
#### Daily Coding Problem: Problem #373 [Hard]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Facebook.
Given a list of integers L, find the maximum length of a sequence of consecutive numbers that can be formed using elements from L.
For example, given L = [5, 2, 99, 3, 4, 1, 100], return 5 as we can build a sequence [1, 2, 3, 4, 5] which has length 5.
```
[*code*](codesPython/coding373.py)

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
#### Daily Coding Problem: Problem #561 [Hard]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Etsy.
Given a sorted array, convert it into a height-balanced binary search tree.
```
[*code*](codesPython/coding561.py)

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
#### Daily Coding Problem: Problem #578 [Easy] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Bloomberg.
Determine whether there exists a one-to-one character mapping from one string s1 to another s2.
For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.
Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
```
[*code*](codesPython/coding578.py)

---
#### Daily Coding Problem: Problem #580 [Easy] 
```
Good morning! Here's your coding interview problem for today.
This question was asked by Apple.
Given a binary tree, find a minimum path sum from root to a leaf.
For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.
  10
 /  \
5    5
 \     \
   2    1
       /
     -1
```
[*code*](codesPython/coding580.py)

---
#### Daily Coding Problem: Problem #581 [Easy]
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
#### Daily Coding Problem: Problem #585 [Medium] 
```
Good morning! Here's your coding interview problem for today.
This question was asked by Google.
Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing only 1's and return its area.
For example, given the following matrix:
[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]
Return 4.
```
[*code*](codesPython/coding585.py)

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
#### Daily Coding Problem: Problem #602 [Medium] 
```
Daily Coding Problem: Problem #602 [Easy]
Good morning! Here's your coding interview problem for today.
This problem was asked by Facebook.
Suppose you are given two lists of n points, one list p1, p2, ..., pn on the line y = 0 and the other list q1, q2, ..., qn on the line y = 1. Imagine a set of n line segments connecting each point pi to qi. Write an algorithm to determine how many pairs of the line segments intersect.
```
[*code*](codesPython/coding602.py)

---
#### Daily Coding Problem: Problem #604 [Hard] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Grammarly.
Soundex is an algorithm used to categorize phonetically, such that two names that sound alike but are spelled differently have the same representation.
Soundex maps every name to a string consisting of one letter and three numbers, like M460.
One version of the algorithm is as follows:
1.	Remove consecutive consonants with the same sound (for example, change ck -> c).
2.	Keep the first letter. The remaining steps only apply to the rest of the string.
3.	Remove all vowels, including y, w, and h.
4.	Replace all consonants with the following digits:
o	b, f, p, v → 1
o	c, g, j, k, q, s, x, z → 2
o	d, t → 3
o	l → 4
o	m, n → 5
o	r → 6
5.	If you don't have three numbers yet, append zeros until you do. Keep the first three numbers.
Using this scheme, Jackson and Jaxen both map to J250.
Implement Soundex.
```
[*code*](codesPython/coding604.py)

---
#### Daily Coding Problem: Problem #619 [Easy]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Coursera.
Given a 2D board of characters and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
For example, given the following board:
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
```
[*code*](codesPython/coding619.py)

---
#### Daily Coding Problem: Problem #631 [Easy]
```
Daily Coding Problem: Problem #631 [Hard]
Good morning! Here's your coding interview problem for today.
This problem was asked by VMware.
The skyline of a city is composed of several buildings of various widths and heights, possibly overlapping one another when viewed from a distance. We can represent the buildings using an array of (left, right, height) tuples, which tell us where on an imaginary x-axis a building begins and ends, and how tall it is. The skyline itself can be described by a list of (x, height) tuples, giving the locations at which the height visible to a distant observer changes, and each new height.
Given an array of buildings as described above, create a function that returns the skyline.
For example, suppose the input consists of the buildings [(0, 15, 3), (4, 11, 5), (19, 23, 4)]. In aggregate, these buildings would create a skyline that looks like the one below. 
     ______  
    |      |        ___
 ___|      |___    |   | 
|   |   B  |   |   | C |
| A |      | A |   |   |
|   |      |   |   |   |
------------------------
As a result, your function should return [(0, 3), (4, 5), (11, 3), (15, 0), (19, 4), (23, 0)].
```
[*code*](codesPython/coding631.py)

---
#### Daily Coding Problem: Problem #634 [Easy]
```
Daily Coding Problem: Problem #634 [Medium]
Good morning! Here's your coding interview problem for today.
This problem was asked by Square.
You are given a histogram consisting of rectangles of different heights. These heights are represented in an input list, such that [1, 3, 2, 5] corresponds to the following diagram:
      x
      x  
  x   x
  x x x
x x x x
Determine the area of the largest rectangle that can be formed only from the bars of the histogram. For the diagram above, for example, this would be six, representing the 2 x 3 area at the bottom right.
```
[*code*](codesPython/coding634.py)

---
#### Daily Coding Problem: Problem #637 [Easy]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Snapchat.
Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.
The input list is not necessarily ordered in any way.
For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], 
you should return [(1, 3), (4, 10), (20, 25)].
```
[*code*](codesPython/coding637.py)

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
#### Daily Coding Problem: Problem #642 [Easy]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Pivotal.
A step word is formed by taking a given word, adding a letter, and anagramming the result. For example, starting with the word "APPLE", you can add an "A" and anagram to get "APPEAL".
Given a dictionary of words and an input word, create a function that returns all valid step words.
```
[*code*](codesPython/coding642.py)

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
#### Daily Coding Problem: Problem #646 [Medium] 
```
Daily Coding Problem: Problem #646 [Easy]
Good morning! Here's your coding interview problem for today.
This problem was asked by Twitter.
A classroom consists of N students, whose friendships can be represented in an adjacency list. For example, the following descibes a situation where 0 is friends with 1 and 2, 3 is friends with 6, and so on.
{0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]} 
Each student can be placed in a friend group, which can be defined as the transitive closure of that student's friendship relations. In other words, this is the smallest set such that no student in the group has any friends outside this group.
For the example above, the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.
Given a friendship list such as the one above, determine the number of friend groups in the class.
```
[*code*](codesPython/coding646.py)

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
#### Daily Coding Problem: Problem #651 [Medium]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by LinkedIn.
Determine whether a tree is a valid binary search tree.
A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.
```
[*code*](codesPython/coding651.py)

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
### Daily Coding Problem: Problem #658 [Hard]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.
```
[*code*](codesPython/coding658.py)

---
### Daily Coding Problem: Problem #660 [Hard] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Airbnb.
You come across a dictionary of sorted words in a language you've never seen before. Write a program that returns the correct order of letters in this language.
For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], you should return ['x', 'z', 'w', 'y'].
```
[*code*](codesPython/coding660.py)

---
### Daily Coding Problem: Problem #661 [Hard] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Airbnb.
You come across a dictionary of sorted words in a language you've never seen before. Write a program that returns the correct order of letters in this language.
For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], you should return ['x', 'z', 'w', 'y'].
```
[*code*](codesPython/coding661.py)

---
### Daily Coding Problem: Problem #662 [Easy]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Amazon.
Given n numbers, find the greatest common denominator between them.
For example, given the numbers [42, 56, 14], return 14.
```
[*code*](codesPython/coding662.py)

---
### Daily Coding Problem: Problem #665 [Easy] 
```
Daily Coding Problem: Problem #665 [Easy] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Amazon.
Given n numbers, find the greatest common denominator between them.
For example, given the numbers [42, 56, 14], return 14.
```
[*code*](codesPython/coding665.py)

---
### Daily Coding Problem: Problem #668 [Easy]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.
Here is an example:
1 2 3 4 8
5 1 2 3 4
4 5 1 2 3
7 4 5 1 2
Write a program to determine whether a given input is a Toeplitz matrix.
```
[*code*](codesPython/coding668.py)

---
### Daily Coding Problem: Problem #669 [Hard]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
The game of Nim is played as follows. Starting with three heaps, each containing a variable number of items, two players take turns removing one or more items from a single pile. The player who eventually is forced to take the last stone loses. For example, if the initial heap sizes are 3, 4, and 5, a game could be played as shown below:
  A  |  B  |  C
-----------------
  3  |  4  |  5
  3  |  1  |  3
  3  |  1  |  3
  0  |  1  |  3
  0  |  1  |  0
  0  |  0  |  0 
In other words, to start, the first player takes three items from pile B. The second player responds by removing two stones from pile C. The game continues in this way until player one takes last stone and loses.
Given a list of non-zero starting values [a, b, c], and assuming optimal play, determine whether the first player has a forced win.
```
[*code*](codesPython/coding669.py)

---
### Daily Coding Problem: Problem #670 [Medium]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Facebook.
Given a positive integer n, find the smallest number of squared integers which sum to n.
For example, given n = 13, return 2 since 13 = 3^2 + 2^2 = 9 + 4.
Given n = 27, return 3 since 27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9.
```
[*code*](codesPython/coding670.py)

---
### Daily Coding Problem: Problem #673 [Hard]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by LinkedIn.
Given a list of points, a central point, and an integer k, find the nearest k points from the central point.
For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].
```
[*code*](codesPython/coding673.py)

---
### Daily Coding Problem: Problem #674 [Easy]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
A girl is walking along an apple orchard with a bag in each hand. She likes to pick apples from each tree as she goes along, but is meticulous about not putting different kinds of apples in the same bag.
Given an input describing the types of apples she will pass on her path, in order, determine the length of the longest portion of her path that consists of just two types of apple trees.
For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, with a length of four.
```
[*code*](codesPython/coding674.py)

---
### Daily Coding Problem: Problem #677 [Easy]
```
Good morning! Here's your coding interview problem for today.
This problem was asked by Square.
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. The method is to take increasingly larger prime numbers, and mark their multiples as composite. 
For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. 
Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.
Implement this algorithm.
Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).
```
[*code*](codesPython/coding677.py)

---
### Daily Coding Problem: Problem #678 [Easy] 
```
Good morning! Here's your coding interview problem for today.
This problem was asked by IBM.
Given an integer, find the next permutation of it in absolute order. For example, given 48975, the next permutation would be 49578.
```
[*code*](codesPython/coding678.py)

---