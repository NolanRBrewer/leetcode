from heapq import *
import heapq

class SlidingWindowMedian:
    def __init__(self) -> None:
        self.maxHeap, self.minHeap = [], []
    
    def find_sliding_window_median(self, nums, k):
        result = [0.0 for x in range(len(nums)- k + 1)]
        for i in range(0, len(nums)):
            if not self.maxHeap or nums[i] <= -self.maxHeap[0]:
                heappush(self.maxHeap, -nums[i])
            else:
                heappush(self.minHeap, nums[i])
            
            self.rebalance_heaps()

            if i - k + 1 >= 0:
                if len(self.maxHeap) == len(self.minHeap):
                    result[i - k + 1] = -self.maxHeap[0]/ 2.0 + self.minHeap[0]/2.0
                else:
                    result[i - k + 1] = -self.maxHeap[0] / 1.0

                elementToBeRemoved = nums[i - k + 1]
                if elementToBeRemoved <= -self.maxHeap[0]:
                    self.remove(self.maxHeap, -elementToBeRemoved)
                else:
                    self.remove(self.minHeap, elementToBeRemoved)

                self.rebalance_heaps()
        return result   

    def remove(self, heap, element):
        ind = heap.index(element)

        heap[ind] = heap[-1]
        del heap[-1]

        if ind < len(heap):
            heapq.heapify(heap)

    def rebalance_heaps(self):
        # favor max heap if an odd number of items are held between both heaps.
        if len(self.maxHeap) > len(self.minHeap) -1:
            heappush(self.minHeap,-heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxheap, -heappop(self.minHeap))


def main():

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()