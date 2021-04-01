no_of_games = int(input())
games = input()
anton = 0
danik = 0
for i in range(no_of_games):
    if games[i] == "A":
        anton += 1
    else:
        danik += 1


if anton > danik:
    print("Anton")
elif danik > anton:
    print("Danik")
elif anton == danik:
    print("Friendship")