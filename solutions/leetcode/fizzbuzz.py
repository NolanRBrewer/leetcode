def fizzbuzz_chal(nums):    
    fizzbuzz = []
    for i in range(nums):
        if i % 15 == 0:
            fizzbuzz.append('fizzbuzz')
        elif i % 5 == 0:
            fizzbuzz.append('buzz')
        elif i % 3 == 0:
            fizzbuzz.append('fizz')
        else:
            fizzbuzz.append(i)
    return fizzbuzz

print(fizzbuzz_chal(100))