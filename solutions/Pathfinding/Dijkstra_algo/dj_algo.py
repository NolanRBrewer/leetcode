'''
Steps to to Dijkstra's Algorithm:
----------------------------------
1. Mark all Nodes unvisited

i.e. put everry node into an set labeled unvisited.
-----------------------------------
2. Assign a tentative distance value to every node.

The initial node will be assigned 0, because the distance from our position to the start is
0. All other nodes will be marked infinite float('inf')
-----------------------------------
3. Consider all of the current node's neighbors and mark the tentative distance


'''


def shortest_distance(new_map,start,destination):
    unvisited = label_unvisited(new_map)
    distances = {}
    assign_distance(unvisited, start, distances)
    bfs(new_map, distances, unvisited, destination)

def label_unvisited(new_map):
    q = set()
    for x in range(len(new_map)):
        for y in range(len(new_map[-1])):
            q.add((x,y))
    return q

def assign_distance(queue, start,distances):
    for coord in queue:
        if coord == start:
            distances[coord] = 0
        else:
            distances[coord] = float('inf')

def bfs(new_map, distances, unvisited, destination):
    '''
    For example, if the current node A is marked with a distance of 6, 
    and the edge connecting it with a neighbor B has length 2, then the distance to B through A 
    will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change it to 8. 
    Otherwise, the current value will be kept.
    '''
    
    while unvisited:
        valid_distances = [(distances[point], point) for point in unvisited if distances[point] != float('inf')]
        # error here
        if not valid_distances:
            return "Destination unreachable"
        pos = min(valid_distances, key=lambda x: x[0])[1]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        # check for pos being the destination
        if pos == destination:
            # When we reach the destination return the distance
            return distances[pos]
        else:
            # Otherwise, select the unvisited node that is marked with the smallest tentative distance, 
            # set it as the new current node
            for direction in directions:
                xx = pos[0] + direction[0]
                yy = pos[1] + direction[1]
                # add 1 for each 'layer' stepped out
                if (xx,yy) in unvisited and new_map[xx][yy] != 1:
                    if distances[(xx,yy)] < distances[pos] + 1:
                        distances[(xx,yy)] = distances[pos] + 1
            unvisited.remove(pos)#remove after checking all neighbors
    return "Destination Invalid"

def main():
    new_map = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1],
    ]

    # Valid and reachable starting and destination points
    starting_point = (1, 1)
    destination_point = (4, 7)
    print("shortest distance between points is" + str(shortest_distance(new_map, starting_point, destination_point)))

main()

