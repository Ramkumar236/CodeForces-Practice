level = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
completed = []
for i in range(1, p[0]+1):
    completed.append(p[i])
for i in range(1, q[0]+1):
    if q[i] in completed:
        continue
    else:
        completed.append(q[i])
if len(completed) == level:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")