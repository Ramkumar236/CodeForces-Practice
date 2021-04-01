n = int(input())
grp = []
count = 1
for i in range(0, n):
    grp.append(input())
    if i == 0:
        continue
    elif grp[i-1] == "10" and grp[i] == "01" or grp[i-1] == "01" and grp[i] == "10":
        count += 1
print(count)