from collections import deque

def increasing_monotonic_queue(arr, n):
    q = deque()
    for i in range(n):
        while q and q[-1] > arr[i]:
            q.pop()
        q.append(arr[i]) 
    return q
 
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
q = increasing_monotonic_queue(arr, n)
for i in q:
    print(i, end=' ')