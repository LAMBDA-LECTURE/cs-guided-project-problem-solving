"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str: str) -> int:
    # Your code here
    # keep a list/string of all the vowels
    vowels = "aeiou"
    # vowels = [a, e, i, o, u] # also a valid way
    # count number of vowels in a counter
    num_vowels = 0
    # inspect every character (we don't care about indices)
    for char in input_str:
        # is it a vowel
        # how do we know if it's a vowel
        if char in vowels:
            num_vowels += 1
        #googlesays : no builtin method
    # return our counter
    return num_vowels

print(get_count("hakuna matata"))
print(get_count("qwertyuioplkjhgfdsazxcvbnm"))