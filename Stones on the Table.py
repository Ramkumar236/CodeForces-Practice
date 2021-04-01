num = int(input())
colors = list(map(str,input()))
count = 0
for i in range(num-1):
    if colors[i] == colors[i+1]:
        count += 1
print(count)