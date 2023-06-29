'''
POINTS OF MISUNDERSTANDING:
    why are max heap references done with '-' in front?
'''
from heapq import *

class MedianOfAStream:
    maxHeap = []
    minHeap = []
    def insert_num(self,num):
        #if nothing in max heap or if the smallest value 
        # in max heap is greater than the num
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)
        # if the max heap is more than one item greater than
        # the min heap, move one item from the max heap to the min heap.
        if len(self.maxHeap) > len(self.minheap)+ 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        # vice versa if the min heap is ever larger than max heap
        elif len(self.maxHeap) < len(self.minheap):
            heappush(self.maxHeap, heappop(self.minHeap))

    def find_median(self):

        if len(self.maxHeap) == len(self.minheap):
            # take the average of middle elements if heaps have same length
            return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0
        
        return -self.maxHeap[0] / 1.0 # returns with decimal place