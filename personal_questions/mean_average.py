# create a function that returns the average of a list.
numbers = [76,81,53,7,8,24,90,26,37,46,5,4] 

def rounded_average(number_list):
    total = 0
    for number in number_list:
        total += number
    average = total // len(number_list)
    return average

print(rounded_average(numbers))