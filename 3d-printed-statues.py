statues = int(input())
printers = 1
days = 0

while printers < statues:
    printers *= 2
    days += 1

days += 1
print(days)
