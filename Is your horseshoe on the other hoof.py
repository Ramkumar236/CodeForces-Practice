shoes = list(map(int,input().split()))
remove_duplicate = set(shoes)
minimum_shoes = 4-len(remove_duplicate)
print(minimum_shoes)


