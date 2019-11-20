n = int(input())

for i in range(n):
    years = input().split(" ")
    x = 0
    for j in range(len(years)):
        if int(years[j]) != 0 and int(years[j]) * 2 < int(years[j+1]):
            x += int(years[j + 1]) - (int(years[j]) * 2)
    print(x)
