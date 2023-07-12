from heapq import *

def find_k_largest_num(nums, k):
    MinHeap = []

    for i in range(k):
        heappush(MinHeap,nums[i])

    for i in range(k, len(nums)):
        if nums[i] > MinHeap[0]:
            heappop(MinHeap)
            heappush(MinHeap, nums[i])
        
    return MinHeap

def main():

  print("Here are the top K numbers: " +
        str(find_k_largest_num([3, 1, 5, 12, 2, 11], 3)))

  print("Here are the top K numbers: " +
        str(find_k_largest_num([5, 12, 11, -1, 12], 3)))


main()
