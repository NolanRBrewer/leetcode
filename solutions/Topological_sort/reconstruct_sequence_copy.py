
from collections import deque

def can_construct(original_sequence, sequences):
    sorted_order = []
    if len(original_sequence) <= 0:
        return False
    
    graph = {}
    inDegrees = {}

    for sequence in sequences:
        for num in sequence:
            inDegrees[num] = 0
            graph[num] = []
    
    for sequence in sequences:
        for i in range(1,len(sequence)):
            start, end = sequence[i -1], sequence[i]
            graph[start].append(end)
            inDegrees[end] += 1
    
    sources = deque()
    for key in inDegrees:
        if inDegrees[key] == 0:
            sources.append(key)
    
    while sources:
        if len(sources) > 1:
            return False
        if original_sequence[len(sorted_order)] != sources[0]:
            return False
        


def main():
    print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
    print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
    print("Can construct: " +
        str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()
