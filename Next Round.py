num_of_participants, k_postion = input().split()
lst = list(map(int, input().split()))
count=0
for i in range(int(num_of_participants)):
    if lst[i]>0 and lst[i]>= lst[int(k_postion)-1]:
        count = count+1
print(count)