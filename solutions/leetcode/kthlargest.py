'''
Writing a heap

'''
from typing import *
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = Heap(nums) 
        self.k = k
        

    def add(self, val: int) -> int:
        while len(self.heap.heap) > self.k:
            self.heap.heap.pop()
        self.heap.insert(val)
        return self.heap.heap(self.k)
        
    
class Heap:
    def __init__(self, nums:List[int]):
        self.heap = []
        for num in nums:
            self.insert(num)

    def find_max(self) -> int:
        '''
        find the largest element in the heap
        '''
        return self.heap[0]

    def insert(self, val):
        self.heap.append(val) # 1, 67, 
        parent_index = (len(self.heap) -1) // 2
        parent = self.heap[parent_index]
        while val > parent:
            self.heap[-1] = parent
            self.heap[parent_index] = val
            parent_index = self.parent(parent_index)
            parent = self.heap[parent_index]
        

    def parent(self, pos):
         return pos // 2

    def sort(self):
        '''
        switch the parent with largest of its two children if the parent is less than the child.
        '''
        '''
        smaller of the children being greater than 
        '''
        pos = 0 #1, 4, 
        position_grouping = list(enumerate(self.heap))
        parent_index, parent =  list(enumerate(self.heap))[pos]#(0, 100)
        
        # max comparison
        child_index, max_child = max(position_grouping[self.leftchild(pos)], position_grouping[self.rightchild(pos)], key= lambda element: element[1])
        
        
        while max_child > parent:
            self.heap[pos], self.heap[child_index] = self.heap[child_index], self.heap[pos]
            pos = child_index
            child_index, max_child = max(position_grouping[self.leftchild(pos)], position_grouping[self.rightchild(pos)], key= lambda element: element[1])

    def leftchild(self, pos):
        return (pos * 2) + 1

    def rightchild(self, pos):
        return (pos * 2) + 2


nums = [1,67,3,45,26]

heap = Heap(nums)

print(heap.insert(4))