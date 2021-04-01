num = int(input())
bill = 0
while num:
    if num>=100:
        bill += num//100
        num = num-num//100*100
    elif num>=20:
        bill += num // 20
        num = num - num // 20*20
    elif num>=10:
        bill += num // 10
        num = num - num // 10*10
    elif num>=5:
        bill += num // 5
        num = num - num // 5*5
    else:
        bill+=num
        num=0
print(bill)