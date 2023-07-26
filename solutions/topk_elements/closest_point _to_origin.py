'''
Given an array of points in a 2D2D plane, find ‘K’ closest points to the origin.

Example 1:

Input: points = [[1,2],[1,3]], K = 1
Output: [[1,2]]
Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
The Euclidean distance between (1, 3) and the origin is sqrt(10).
Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.
'''
from __future__ import print_function
from heapq import *
class Point:
    def __init__(self , x, y) -> None:
        # create point object identified by its coordinates
        self.x  = x
        self.y = y
    
    # used for max-heap
    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    def distance_from_origin(self):
        # ignoring sqrt to calculate the distance
        return (self.x * self.x) + (self.y * self.y)

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

def find_closest_points(points, k):
    maxHeap = []
    for i in range(k):
        heappush(maxHeap, (-points[i].distance_from_origin(), points[i]))

    for i in range(k, len(points)):
        distance = points[i].distance_from_origin()
        if distance < -maxHeap[0][0]:
            heappop(maxHeap)
            heappush(maxHeap, (-distance, points[i]))

    closestPoints = []
    while maxHeap:
        closestPoints.append(maxHeap[0][1])
        heappop(maxHeap)

    return closestPoints
    
def main():
    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()

main()