from collections import deque
'''
Time Complexity:
    O(V + E)
    V = number of letters in language
    E = the number of edges (relationships) between each of the letters

Space Complexity:
    0(V + N) = total space of adjacency list
    V = each letter
    N = relations for each letter
'''

def find_order(words):
    
    # initialize graph
    inDegrees = {}
    graph = {}
    for word in words:
        for char in word:
            graph[char] = []
            inDegrees[char] = 0


    # populate graph
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        for j in range(min(len(w1), len(w2))):
            start, end = w1[j], w2[j]
            if start != end:
                graph[start].append(end)
                inDegrees[end] += 1
                break 
    
    sources = deque()
    # populate sources
    for key in inDegrees:
        if inDegrees[key] == 0:
            sources.append(key)
    
    sorted_order = []
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for end in graph[vertex]:
            inDegrees[end] -= 1
            if inDegrees[end] == 0:
                sources.append(end)
    
    if len(sorted_order) != len(inDegrees):
        return []

    return "".join(sorted_order)

def main():
  print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
  print("Character order: " + find_order(["cab", "aaa", "aab"]))
  print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()
