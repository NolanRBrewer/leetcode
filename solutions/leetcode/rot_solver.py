'''
Using your `rot` function, write a function `decrypt` that takes a text encrypted using a shift 
substitution cipher of an unknown shift amount, and returns a tuple containing `(the shift used to 
encrypt the original string, the original string)`.
You will need a dictionary or word list. An input string needs to be long enough to unambiguously 
determine the the shift used, or there could be multiple valid shifts.

Return:
Tuple (shift used, orginal string)

Example:
decrypt("Ju xbt uif cftu pg ujnft, ju xbt uif xpstu pg ujnft") -> 
("It was the best of times, it was the worst of times", 1)
'''
'''
NOTES FOR FUTURE:
        Create (helper) functions for when problems become too large.
        Break down issues to bite sized peices.
'''

def rot(s, shift):
    '''
    Returns proper values on positive shift
    When negative shift is given results are wrong
        - How Modulo works with negative numbers
        - create a base variable to effect the math
    '''
    new_s = ''
    for letter in s:
        if letter.isalpha():
            base = ord('a') if letter.islower() else ord('A')
            shifted_ordinal = (ord(letter) - base + shift) % 26
            shifted_character = chr(shifted_ordinal + base)
            new_s += shifted_character
        else:
            new_s += letter
    return new_s

def decrypt(s, shift= 1):
    '''
    problems:
        - dealing with dding in white space 
        - dealing with punctuation
    
    thoughts:
        looking for a word match for anytime we perform rot shift on our string. 

    approach:
        breakdown the string into individual words, and append them to a list:
            split()

        we can iterate list and perform rot with our current shift for every every word in the list
            Iterate over the string:
                returning the rot(string, shift)

        iteration over word list to see if those in scrabble word bank:
            if the word does match
                confirmed string += word
            if word doesn't match 
                confirmed string = ''
                add one to shift and run rot again
    '''
    if shift >= 26:
        return 'no valid decryption'
    # read in scrabble list
    with open('sowpods.txt') as scrabble_file:
        scrabble_words = [word.strip() for word in scrabble_file]
    
    words = s.split() #split string into individual words
    shifted_words = [] # words after being shifted

    for word in words: #shifting the words
        shifted_words.append(rot(word, shift))

    confirmed_words = [] # the strings that match words in the scrabble list
    for shifted_word in shifted_words:
        '''
        Taking the shifted words and searching for them in the scrabble list.
        checking for characters to be a letter and behaving accordingly for punctuation.
        '''
        if not shifted_word[-1].isalpha():
            last_char = shifted_word[-1]
            shifted_word = shifted_word.strip(last_char)
            if shifted_word.upper() in scrabble_words:
                confirmed_words.append(shifted_word + last_char)
        elif shifted_word.upper() in scrabble_words:
                confirmed_words.append(shifted_word)
        else:
            # update the shift to check one ordinal value greater and recurse.
            return(decrypt(s, shift + 1))

    if confirmed_words:
        return (shift, ' '.join(confirmed_words))

s = "Ju xbt uif cftu pg ujnft, ju xbt uif xpstu pg ujnft"
print(decrypt(s))