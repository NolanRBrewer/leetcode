'''
Given ‘M’ sorted arrays, 
find the smallest range that includes at least one number from each of the ‘M’ lists.

Input: L1=[1, 5, 8], L2=[4, 12], L3=[7, 8, 10]
Output: [4, 7]
Explanation: The range [4, 7] includes 5 from L1, 4 from L2 and 7 from L3.
'''

from heapq import *
# simply for inf and -inf
import math


def find_smallest_range(lists):
    minHeap = []
    # start with largesst possible range 
    rangeStart, rangeEnd = 0, math.inf

    currentMaxNumber = -math.inf

    # put the 1st element of each array in the max heap
    for arr in lists:
        heappush(minHeap, (arr[0], 0, arr))
        currentMaxNumber = max(currentMaxNumber, arr[0])

    # take the smallest(top) element form the min heap, if it gives us smaller range, 
    # update the ranges, if the array of the top element has more elements, insert the 
    # next element in the heap
    while len(minHeap) == len(lists):
        num, i, arr = heappop(minHeap)
        # check if the range is smaller 
        if rangeEnd - rangeStart > currentMaxNumber - num:
            rangeStart = num
            rangeEnd = currentMaxNumber

        # make sure the next index is not out of range
        if len(arr) > i+1:
        # insert the next element in the heap
            heappush(minHeap, (arr[i+1], i+1, arr))
            currentMaxNumber = max(currentMaxNumber, arr[i+1])

    return [rangeStart, rangeEnd]


def main():
  print("Smallest range is: " +
        str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()
