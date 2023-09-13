from collections import deque

def increasing_monotonic_queue(arr, n):
    q = deque()
    for i in range(n):
        while q and q[0] > arr[i]:
            q.pop()
        q.appendleft(arr[i]) # 6, 5, 4  
    return q
 
arr = [1, 2, 5, 4, 5, 6]
n = len(arr)
q = increasing_monotonic_queue(arr, n)
for i in q:
    print(i, end=' ')