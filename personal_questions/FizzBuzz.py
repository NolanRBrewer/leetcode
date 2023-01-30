def fizzBuzz(n):
    fizzbuzz = []
    for num in range(n):
        # if the number is not 0 and is equally divisible by select number
        if num == 0:
            fizzbuzz.append(num)
        elif num % 15 == 0:
            fizzbuzz.append("FizzBuzz")
        elif num % 5 == 0:
            fizzbuzz.append("Buzz")
        elif num % 3 == 0:
            fizzbuzz.append("Fizz")
        else:
            fizzbuzz.append(num)
    return fizzbuzz
print(fizzBuzz(25))