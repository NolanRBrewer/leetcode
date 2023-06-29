'''
Given a word, write a function to generate all of its unique generalized abbreviations.

A generalized abbreviation of a word can be generated by replacing each substring of 
the word with the count of characters in the substring. Take the example of “ab” 
which has four substrings: “”, “a”, “b”, and “ab”. After replacing these substrings 
in the actual word by the count of characters, we get all the generalized abbreviations: 
“ab”, “1b”, “a1”, and “2”.

Note: All contiguous characters should be considered one substring, 
e.g., we can’t take “a” and “b” as substrings to get “11”; since “a” and “b” are contiguous,
we should consider them together as one substring to get an abbreviation “2”.
'''
'''
Input: "BAT"
Output: "BAT", "BA1", "B1T", "B2", "1AT", "1A1", "2T", "3"
'''
from collections import deque

class AbbreviateWord:
    def __init__(self, str, start, wordcount) -> None:
        self.str = str
        self.start = start
        self.wordcount = wordcount

def generate_generalized_abbreviation(word):
    wordlen = len(word)
    result = []
    queue = deque()
    queue.append(AbbreviateWord(list(),0,0))
    while queue:
        abword = queue.popleft()
        if abword.start == wordlen :
            if abword.wordcount != 0:
                abword.str.append(str(abword.wordcount))
            result.append(''.join(abword.str))
        else:
            queue.append(AbbreviateWord(list(abword.str), abword.start + 1, abword.wordcount + 1))

            if abword.wordcount != 0:
                abword.str.append(str(abword.wordcount))

            newWord = list(abword.str)
            newWord.append(word[abword.start])
            queue.append(AbbreviateWord(newWord, abword.start + 1, 0))


def main():
    print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("BAT")))
    print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("code")))


main()