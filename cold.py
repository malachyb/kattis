input()
temps = input().split(" ")
negs = 0

for i in temps:
    if int(i) < 0:
        negs += 1

print(negs)
