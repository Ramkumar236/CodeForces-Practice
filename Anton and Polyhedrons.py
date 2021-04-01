n = int(input())
count = 0
for _ in range(n):
    name = input()
    if name == "Tetrahedron":
        count = count+4
    elif name == "Cube":
        count = count+6
    elif name == "Octahedron":
        count = count+8
    elif name == "Dodecahedron":
        count = count+12
    elif name == "Icosahedron":
        count = count+20
print(count)