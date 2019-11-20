quad = input()
coords = [[0, 0], [1, 0], [0, 1], [1, 1]]
zoom = len(quad)
max_coord = 2 ** zoom

x = 1
y = 1

for i in range(len(quad)):
    x = x * (2 ** coords[int(quad[i])][0]) - 1

print(x)
