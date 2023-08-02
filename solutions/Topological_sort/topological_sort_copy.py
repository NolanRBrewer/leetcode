from collections import deque

def topological_sort(vertices, edges):
    sortedOrder = []
    if vertices <= 0:
       return sortedOrder

    nEdges = {i: 0 for i in range(vertices)} # number of edges incoming
    graph = {i: [] for i in range(vertices)} #connection of parent to children

    for edge in edges:
        # catalogue the parents of chidren, and track the number of edges leading to each child
        parent, child = edge[0], edge[1]

        graph[parent].append(child)
        nEdges[child] += 1
    
    sources = deque()

    for key in nEdges:
        # check for source nodes and add them to the source deque
        if nEdges[key] == 0:
            sources.append(key)

    while sources:
        # FIFO for source checking
        vertex = sources.popleft()
        # add source(s) to sortedOrder
        sortedOrder.append(vertex)
        for child in graph[vertex]:
            # remove one incoming edge as we catalogue a source for this child
            nEdges[child] -= 1
            if nEdges[child] == 0:
                # if we have exhausted all sources for edges leading to this child it becomes a source
                sources.append(child)
        # after every source check, double check to ensure there is not a cycle occuring
        if len(sortedOrder) > vertices:
            # return empty if cycle, because cyclical graphs are invalid
            return []
    # othrewise we can return our sorted order
    return sortedOrder


def main(): 
    print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], \
              [3, 0], [3, 1], [3, 2], [4, 1]])))
    print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1], [1, 3]])))


main()