"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""
def is_even(n):
    return n%2 == 0

def get_middle(input_str):
    # Your code here
    if is_even(len(input_str)):
        # return two middle characters
        midpoint = len(input_str) // 2
        return input_str[midpoint-1:midpoint+1]
    else:
        # return single middle char
        midpoint = len(input_str) // 2
        return input_str[midpoint]

print(get_middle("test")) # -> "es"
print(get_middle("testing")) # -> "t"
print(get_middle("middle")) # -> "dd"
print(get_middle("A")) # -> "A"