from __future__ import print_function
from heapq import *

class ListNode:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
    
    def __lt__(self, other):
        return self.value < other.value
    
def merge_lists(lists):
    minHeap = []
    # since lists are sorted add the root of each list to the heap to allow all values 
    for root in lists:
        if root != None:
            heappush(minHeap, root)
    # After this, we can take out the smallest (top) element from the heap and add it to the merged list.
    resultHead, resultTail = None, None

    while minHeap:
        # After this, we can take out the smallest (top) element from the heap and add it to the merged list.
        node = heappop(minHeap)

        if resultHead == None:

            resultHead = resultTail = node
        else:
            # navigate through lists
            resultTail.next = node
            resultTail = resultTail.next
        
        if node.next is not None:
            heappush(minHeap, node.next)
        
    # return the head of our merged list
    return resultHead


def main():
  l1 = ListNode(2)
  l1.next = ListNode(6)
  l1.next.next = ListNode(8)

  l2 = ListNode(3)
  l2.next = ListNode(6)
  l2.next.next = ListNode(7)

  l3 = ListNode(1)
  l3.next = ListNode(3)
  l3.next.next = ListNode(4)

  result = merge_lists([l1, l2, l3])
  print("Here are the elements form the merged list: ", end='')
  while result is not None:
    print(str(result.value) + " ", end='')
    result = result.next


main()