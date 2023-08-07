'''
Write a function that takes as arguments two strings: `pattern` and `input`. 
Return whether or not `input` can be broken into words to match the pattern of the characters in `pattern`.

(In other words, this is the same problem as part 1, but `input` doesn’t contain spaces, 
so you’ll need to determine if it is possible to split up the input into words in a way 
that matches `pattern`. You will likely want to use recursion.)

EXAMPLEs:
1:
| `pattern: 'abcba'`             |
| ------------------------------ |
| `input: 'redbluegreenbluered'` |
| `result: True`                 |

2:
| `pattern: 'aba'`                                                               |
| ------------------------------------------------------------------------------ |
| `Input: 'xxyyyxx'`                                                             |
| `result: True`, with multiple solutions:<br><br>- x, xyyyx, x<br>- xx, yyy, xx |
'''
'''
finding combinations
    


call word solver
'''

def pattern_solver(pattern,input):
    if len(pattern) == 1:
        return True
    

def separate_input(pattern, s) -> list(str):
    # separate string into a number of words
    valid_seperations = []
    start = 0
    stop = len(s)
    for i in range(stop):
        seperation = (s[start:i+1], s[i+1: stop+1])
        if seperation[0] != s and seperation[1] != s:
            valid_seperations.append(seperation)
    return valid_seperations      
            

def word_solver(pattern, input) -> bool:
    
    matches = {} # which letter matches which color
    full_pattern = set(zip(pattern, separate_input(pattern, input)))

    for letter, color in full_pattern:

        if color not in matches.values():
            matches[letter] = color

    for letter, color in full_pattern:

        if matches.get(letter) != color:
            return False

    return True

def main():

    print(pattern_solver('aba', 'xxyyyxx'))

main()