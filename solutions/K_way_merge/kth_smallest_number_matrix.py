from heapq import *
def kth_smallest_element_in_matrix(matrix, k):
    minHeap = []
    #  adding to a min heap limited to size k is only ever O(logk)
    for i in range(min(k, len(matrix))):
        # add the first element of each row, the index "0", and the row it came from to the heap
        heappush(minHeap, (matrix[i][0], 0, matrix[i]))

    numberCount, number = 0,0
    while minHeap:
        # unpack each tuple
        number, i, row = heappop(minHeap)
        numberCount += 1
        if numberCount == k:
            # leave loop to return when at appropriate number
            break
        elif i+1 < len(row):
            # add the next element in the row with correct index and appropriate row back into the heap
            heappush(minHeap, (row[i+1], i+1, row))
    
    return number

def main():
    print('Kth smallest number is: ' + str(kth_smallest_element_in_matrix([[1,2,4],[3,7,8],[7,8,9]], 5)))
    print('Kth smallest number is: ' + str(kth_smallest_element_in_matrix([[2, 6],[4, 7]], 3)))

main() 
