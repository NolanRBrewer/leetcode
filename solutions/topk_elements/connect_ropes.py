'''
Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost. 
The cost of connecting two ropes is equal to the sum of their lengths.

Example 1:

Input: [1, 3, 11, 5]
Output: 33
Explanation: First connect 1+3(=4), then 4+5(=9), and then 9+11(=20). So the total cost is 33 (4+9+20)
'''

from heapq import *

def cost_to_connect_ropes(lengths):
    minHeap = []

    for i in lengths:
        heappush(minHeap, i)

    result, temp = 0, 0
    while len(minHeap) > 1:
        temp = heappop(minHeap) + heappop(minHeap)
        result += temp
        heappush(minHeap, temp)
    
    return result

def main():
    print("Minimum cost to connect ropes: " +
        str(cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
            str(cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
            str(cost_to_connect_ropes([1, 3, 11, 5, 2])))

main()