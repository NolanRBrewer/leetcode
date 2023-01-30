''' 
create a function that catalogues all the numbers in a list and returns the mode
(the most frequently occuring)
'''
numbers = iter([1,5,2,7,8,5,5,5,4,4,3,6,8,9,1,10,10,2,4])

def find_mode(number_list):
    '''
    1) catalogues numbers upon first occurence
    2) returns the key with the most occurences (mode)
    '''
    num_occurences = {}
    # add nums to dictionary, and add 1 to value if already in list
    for num in number_list:
        if num not in num_occurences:
            num_occurences[num] = 1
        elif num in num_occurences:
            num_occurences[num] += 1
    print(num_occurences)
    # returns key with the most occurences 
    mode = max(num_occurences, key=num_occurences.get)
    mode_value = max(num_occurences.values())
    # mode_with_value = [mode, mode_value]
    return mode, mode_value
print(find_mode(numbers))