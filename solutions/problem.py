n = 121
# x = n %
# print(x)


def palindrome_num(n):
    if str(n) == str(n)[::-1]:
        return True


print(palindrome_num(n))
