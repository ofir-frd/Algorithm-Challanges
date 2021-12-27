# -*- coding: utf-8 -*-
"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.


Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]



---


Runtime: o(n)
    
Runtime: 220 ms
Memory Usage: 18.7 MB

another solution: s[:] = s[::-1]

"""


def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """

    steps = len(s)/2
    if steps % steps == 0:
        steps = int(steps)
    else:
        steps = round(steps+0.5)
        
    for i in range(0, steps, 1):
        s[i], s[len(s)-(i+1)] = s[len(s)-(i+1)], s[i]
        
        
s = ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]
print(s)
reverseString(s)

s = ["h","e","l","l","o"]     
reverseString(s)


s = ["H","a","n","n","a","h"]
reverseString(s)

s = ["a","b","c","d","e","f"]
reverseString(s)
