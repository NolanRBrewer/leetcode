from heapq import *


def find_Kth_smallest(matrix, k):
    minHeap = []

    # put the 1st element of each row in the min heap
    # we don't need to push more than 'k' elements in the heap
    for i in range(min(k, len(matrix))):
        heappush(minHeap, (matrix[i][0], 0, matrix[i]))

    # take the smallest(top) element form the min heap, if the running count is equal to
    # 'k' return the number. If the row of the top element has more elements, add the 
    # next element to the heap
    numberCount, number = 0, 0
    while minHeap:
        # [2 , 0, [2,6]]
        number, i, row = heappop(minHeap)
        print(number)
        numberCount += 1 #1
        if numberCount == k:
            break
        if len(row) > i+1:
            heappush(minHeap, (row[i+1], i+1, row))
    return number


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6], [3, 7]], 3)))

    
main()
