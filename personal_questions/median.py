#  create a function to determine the median values in a set of numbers
numbers = [1,76,81,53,3,8,24,26,90,37,46,2,5,4] 
sorted_numbers = sorted(numbers)
print(sorted_numbers)
# determine median based 
def find_median_element(number_list):

    def even_length_median(number_list):
        median_index = (len(number_list) - 1) // 2
        median_items = (number_list[median_index] + number_list[median_index + 1]) / 2
        return median_items

    def odd_length_median(number_list):
        median_index = (len(number_list) - 1) // 2
        median_item = number_list[median_index]
        return median_item

    if len(number_list) % 2 == 0:
        print(even_length_median(sorted_numbers))

    elif len(number_list) % 2 != 0:
        print(odd_length_median(sorted_numbers))


print(find_median_element(sorted_numbers))