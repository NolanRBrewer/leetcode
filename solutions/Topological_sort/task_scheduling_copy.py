'''
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. 
Each task can have some prerequisite tasks which need to be completed before 
it can be scheduled. Given the number of tasks and a list of prerequisite pairs,
 find out if it is possible to schedule all the tasks.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: true
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs 
to finish before '2' can be scheduled. One possible scheduling of tasks is: [0, 1, 2] 
'''
from collections import deque

def is_scheduling_possible(tasks, prereqs):
    sortedOrder = []
    if tasks <= 0:
        return sortedOrder
    
    nEdges = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    for prereq in prereqs:
        parent, child = prereq[0], prereq[1]
        nEdges[child] += 1
        graph[parent].append(child)
        
    sources = deque()
    for key in nEdges:
        if nEdges[key] == 0:
            sources.append(key)
    
    while sources:
        # FIFO
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:
            nEdges[child] -= 1
            if nEdges[child] == 0:
                sources.append(child)

    return tasks == len(sortedOrder)

def main():
    print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))

main()