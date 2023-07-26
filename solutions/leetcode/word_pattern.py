'''
word solver:
Write a function that takes as arguments two strings: pattern and input. 
Return whether or not the words in input match the pattern of the characters in pattern.

examples:
| `pattern: 'abba'`            |
| ---------------------------- |
| `input: 'red blue blue red'` |
| `result: True`               |
---------------------------------
| `pattern: 'abba'`             |
| ----------------------------- |
| `Input: 'red blue green red'` |
| `result: False`               |

pattern: 'abcabdc'
input:'red blue green red blue green green'
result: False
'''
'''
fail:
zip pattern, and input 
turn the zip into a set
check if the length of the zip_set is equal to the length of set(pattern)
    return boolean

next:

list of zip pattern and input
create dictionaries for matches, and letter count

iterate over pattern
    count letters with a dictionary

iterate over zip list 
    enter each match into matches dictionary 
    to have as the correlation between each letter

'''
def word_solver(pattern, input) -> bool:
    
    input_pattern = input.split()
    matches = {} # which letter matches which color
    full_pattern = set(zip(pattern, input_pattern))

    for letter, color in full_pattern:

        if color not in matches.values():
            matches[letter] = color

    for letter, color in full_pattern:

        if matches.get(letter) != color:
            return False

    return True

print(word_solver('abcabd', 'red blue green red blue green')) #False
print(word_solver('abcab', 'red blue green red blue')) #True
print(word_solver('abba', 'red blue green red')) #False !!!!
print(word_solver('abcabdc', 'red blue green red blue green green')) #False