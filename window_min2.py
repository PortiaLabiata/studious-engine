from collections import deque
n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

res = []
q = deque()
for i in range(0, n):
    if len(q) > 0 and q[0] <= i - k:
        q.popleft()
    while len(q) > 0 and a[q[-1]] >= a[i]:
        q.pop()
    q.append(i)
    if i >= k - 1:
        res.append(a[q[0]])

print(*res, sep='\n')
