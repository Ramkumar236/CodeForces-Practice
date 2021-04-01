n1 = list(map(str,input()))
n2 = list(map(str, input()))
final = list(map(str,input()))
n1.extend(n2)
n1= sorted(n1)
final = sorted(final)

flag=0
if len(n1)==len(final):
    for i in range(len(final)):
        if n1[i] == final[i]:
            continue
        else:
            flag = 1
            break
    if flag == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")