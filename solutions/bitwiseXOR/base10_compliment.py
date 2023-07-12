'''
create a function that 
'''

def find_complement(num):
    bit_count = 0
    n = num
    # find the number of active bits
    while n > 0:
        bit_count += 1
        n  = n >> 1
    # use the bit count to calculate the bit set of the complimentary number
    bit_set =  pow(2, bit_count) -1
    print(bit_set)
    # XOR num with the bit set to return the compliment value
    return num ^ bit_set

def main():
    print(f'Complement to your number is: ' + str(find_complement(8)))
    print(f'Complement to your number is: ' + str(find_complement(10)))
    print(f'Complement to your number is: ' + str(find_complement(17)))

main()