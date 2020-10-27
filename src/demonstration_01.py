"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""
from typing import List

def last(a: List[int], n: int) -> List[int]:
    # Your code here
    # if n is longer than the length of the list, return invalid
    if n > len(a):
        return "invalid"
    else:
        # return the last n elements as a list of ints
        # similiar: how would we do this if we needed to return the first n elements?
        # grab everything from index0 up to n
        # grab a subslice, starting at beginning of our input & having len(n)

        # python's slicing syntax:   a[0:n]
        # to get last n elements
        # we want to start slicing from len(a)-n and take everything to the end of list
        # a[len(a) - n:]
        return a[len(a) - n:]
        # return a[-n:] #fails when n=0, would need another if catch for 0
        # JS/TS syntax:  a.slice(0,n)
        # a.slice(n)

print(last([1, 2, 3, 4, 5], 1)) # ➞ [5]
print(last([4, 3, 9, 9, 7, 6], 3)) # ➞ [9, 7, 6]
print(last([1, 2, 3, 4, 5], 7)) # ➞ "invalid"
print(last([1, 2, 3, 4, 5], 0)) # ➞ []