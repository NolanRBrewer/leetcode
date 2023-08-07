from collections import deque
def topological_sort(vertices, edges):
    sortedOrder =[]

    nEdges = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    for edge in edges:
        start, end = edge[0], edge[1]
        nEdges[end] += 1 
        graph[start].append(end) 

    sources = deque()
    '''
    when BFS use a queue and iterative approach
    when DFS use recursion 
    ''' 
    for key in nEdges:
       if nEdges[key] == 0:
          sources.append(key)
    
    while sources:
    #    FIFO
        source = sources.popleft()
        sortedOrder.append(source)
        for end in graph[source]:
            nEdges[end] -= 1
            if nEdges[end] == 0:
                sources.append(end)

        if len(sortedOrder) > vertices:
           return []
        
    return sortedOrder
  


def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], \
              [3, 0], [3, 1], [3, 2], [4, 1]])))


main()