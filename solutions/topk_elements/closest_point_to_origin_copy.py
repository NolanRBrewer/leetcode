from __future__ import print_function
from heapq import * 

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()
    
    def distance_from_origin(self):
        # calculate without square root to find distance
        return (self.x * self.x) + (self.y * self.y)
    
    def print_point(self):
        print("[" + str(self.x)+ ","+ str(self.y) + "]", end='')

def find_closest_points(points, k):
    maxHeap = []
    for i in range(k):
        heappush(maxHeap, (-points[i].distance_from_origin(), points[i]))
    
    for i in range(k, len(points)):
        distance = points[i].distance_from_origin()
        if distance < -maxHeap[0][0]:
            # after checking for a shorter distance replace the 
            heappop(maxHeap)
            heappush(maxHeap, (-distance, points[i]))

    closest_points = []
    while maxHeap:
        closest_points.append(maxHeap[0][1])
        heappop(maxHeap)

    return closest_points


def main():
    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()

main()