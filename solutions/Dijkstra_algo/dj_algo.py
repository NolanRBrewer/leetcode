map = [[1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,1],
       [1,0,0,1,1,0,0,0,1],
       [1,0,0,0,1,0,0,0,1],
       [1,0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1,1],
       ]

def shortest_distance(map,start,end):
    unvisited = unvisited(map)
    distances = {}
    assign_distance(unvisited, start, distances)
    bfs(distances, unvisited)

def unvisited(map):
    q = set()
    for x in range(len(map)):
        for y in range(len(map[-1])):
            q.add((x,y))
    return q

def assign_distance(queue, start,distances):
    for coord in queue:
        if coord == start:
            distances[coord] = 0
        else:
            distances[coord] = float('inf')

def bfs(distances, unvisited, destination):
    '''
    For example, if the current node A is marked with a distance of 6, 
    and the edge connecting it with a neighbor B has length 2, then the distance to B through A 
    will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change it to 8. 
    Otherwise, the current value will be kept.
    '''
    
    while unvisited:
        pos = min([(distances[point], point) for point in unvisited if distances[point] != float('inf')], lambda x: x[0])[1]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        # check for pos being the destination
        if pos == destination:
            pass
        else:
            # Otherwise, select the unvisited node that is marked with the smallest tentative distance, 
            # set it as the new current node
            for direction in directions:
                xx = pos[0] + direction[0]
                yy = pos[1] + direction[1]
                # add 1 for each 'layer' stepped out
                if (xx,yy) in unvisited and (xx,yy) != 1:
                    if distances[(xx,yy)] < distances[pos] + 1:
                        distances[(xx,yy)] = distances[pos] + 1
            unvisited.remove(pos)#remove after checking all neighbors



