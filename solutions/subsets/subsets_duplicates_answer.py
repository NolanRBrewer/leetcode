def find_subsets(nums):
  # sort the numbers to handle duplicates
  list.sort(nums)
  subsets = []
  subsets.append([])
  startIndex, endIndex = 0, 0
  for i in range(len(nums)):
    startIndex = 0 
    
    if i > 0 and nums[i] == nums[i - 1]: # if current and the previous elements are same,
      startIndex = endIndex + 1
    endIndex = len(subsets) - 1 # never exceed the length of our subsets
    #  create new subsets only from the subsets added in the previous step
    for j in range(startIndex, endIndex+1):
      # start and end index iterates through only the new subsets
      # add the number to the new subsets which were created in the previous step
      set1 = list(subsets[j]) #create a deep copy of the subset at j
      set1.append(nums[i]) # add the current number to the subset copy
      # add the new subsets to our list of subsets
      subsets.append(set1)
  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
