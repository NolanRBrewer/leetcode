from collections import deque

def print_orders(tasks, prereqs):
    sorted_order = []
    if tasks <= 0:
        return False
    # graph set up
    inDegrees = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    for prereq in prereqs:
        start, end = prereq[0], prereq[1]
        inDegrees[end] += 1
        graph[start].append(end)

    sources = []
    for key in inDegrees:
        if inDegrees[key] == 0:
            sources.append(key)
    print_all_task_schedules(graph, inDegrees, sources, sorted_order)

def print_all_task_schedules(graph, inDegrees, sources, sorted_order): 

    if sources:
        for source in sources:
            sorted_order.append(source)
            sources_for_next_call = deque(sources)
            sources_for_next_call.remove(source)
            # add children to sources for the next call as they become valid
            for end in graph[source]:
                inDegrees[end] -= 1
                if inDegrees[end] == 0:
                    sources_for_next_call.append(end)
            # recursive call
            print_all_task_schedules(graph, inDegrees, sources_for_next_call, sorted_order)

            # backtracking

            sorted_order.remove(source)
            # add the incoming edge back for each end point
            for end in graph[source]:
                inDegrees[end] += 1
    # If sorted order doesn't have an equal number of items as inDegrees we either:
    # A. have not processed all tasks in this call or,
    # B. have a cyclic dependency making the schedule invalid
    if len(sorted_order) == len(inDegrees):
        print(sorted_order)


def main():
    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])

    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()