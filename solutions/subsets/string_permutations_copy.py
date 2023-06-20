def string_case_premutation(str):
    permutations = []
    permutations.append(str)

    for i in range(len(str)):
        if str[i].isalpha():

            n = len(permutations)
            for j in range(n):
                chs = list(permutations[j])
                chs[i] = chs[i].swapcase()
                permutations.append(''.join(chs))
    return permutations




def main():
    print("String permutations are: " +
        str(string_case_premutation("ad52")))
    print("String permutations are: " +
        str(string_case_premutation("ab7c")))


main()