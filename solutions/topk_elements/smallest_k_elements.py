'''
Given an unsorted array of numbers, find Kth smallest number in it.

Please note that it is the Kth smallest number in the sorted order, 
not the Kth distinct element.

Note: For a detailed discussion about different approaches to solve this problem, 
take a look at Kth Smallest Number.
'''

from heapq import *

def find_k_smallest_num(nums, k):
    MaxHeap = []
    for i in range(k):
        # adding k elements to heap
        heappush(MaxHeap, -nums[i])
    
    for i in range(k, len(nums)):
    # iterate through the remainder of the nums
        if -nums[i] > MaxHeap[0]:
        # if -num is greater than then pop from heap and add the negative of that num to heap 
            heappop(MaxHeap)
            heappush(MaxHeap, -nums[i])
        
    return -MaxHeap[0]

def main():

  print("The k smallest number is: " +
        str(find_k_smallest_num([3, 1, 5, 12, 2, 11], 3)))

  print("The k smallest number is: " +
        str(find_k_smallest_num([5, 12, 11, -1, 12], 3)))


main()