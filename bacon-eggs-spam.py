food = {}
n = int(input())
while n != 0:
    for i in range(n):
        inp = input().split()
        person = inp[0]
        order = inp[1:]
        for item in order:
            if item in food:
                food[item].append(person)
            else:
                food[item] = [person]