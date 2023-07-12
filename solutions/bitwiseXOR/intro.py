'''
XOR is a logical bitwise operator that returns 0 (false) if both bits are the same 
and returns 1 (true) otherwise. 
In other words, it only returns 1 if exactly one bit is set to 1 out of the two bits in comparison.
'''

def find_missing_number(arr):
  n = len(arr) + 1
  # find sum of all numbers from 1 to n.
  s1 = 0
  for i in range (1, n+1):
    s1 += i

  # subtract all numbers in input from sum.
  for i in arr:
    s1 -= i
  
  # s1, now, is the missing number
  return s1

def main():
  arr = [1, 5, 2, 6, 4] 
  print('Missing number is: ' + str(find_missing_number(arr)))

main()
