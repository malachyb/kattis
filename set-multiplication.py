A = [5, 8]
B = ['p', 'q']
C = ['r', 'v']
sets = []

for a in A:
    for b in B:
        for c in C:
            sets.append([a, b, c])
print(sets)
