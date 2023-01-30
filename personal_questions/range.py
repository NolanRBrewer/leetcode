# create a function that calculates the range of a list of numbers.
numbers = [76,81,53,7,8,24,90,26,37,46,5,4,] 
sorted_numbers = sorted(numbers)

def find_range(number_list):
    first_number = 0
    last_number = len(number_list) -1
    range = number_list[last_number] - number_list[first_number]
    return range

print(find_range(sorted_numbers))