from heapq import *
import math

def find_smallest_range(lists):
    minHeap = []
    startRange, endRange = 0, math.inf
    currentMaxNumber = -math.inf

    for arr in lists:
        heappush (minHeap, (arr[0], 0, arr))
        currentMaxNumber = max(currentMaxNumber, arr[0])

    while len(minHeap) == len(lists):
        number, i, arr = heappop(minHeap)
        # check for smaller range
        if endRange - startRange > currentMaxNumber - number:
            # update range
            startRange = number
            endRange = currentMaxNumber
        # check if next index is in range
        if len(arr) > i+1:
            # add next item from array, and appropriate index to the heap
            heappush(minHeap, (arr[i+1], i+1, arr))
            # update the the largest number to the larger of the current max, and the next item in the array
            currentMaxNumber = max(currentMaxNumber, arr[i+1])

    return [startRange, endRange]

def main():
    print("Smallest range is: " + str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()