def find_subsets(nums):
    subsets = [] # [] [1] [3] [1,3]
    subsets.append([])
    for num in nums:
        n = len(subsets)
        for i in range(n):
            set1 = list(subsets[i])
            set1.append(num)
            subsets.append(set1)
    

    return subsets

def main():
   print("Here is the list of subsets: " + str(find_subsets([1, 3])))
   print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()