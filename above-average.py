n = int(input())

for i in range(n):
    successes = 1
    line_in = input().split()
    m = int(line_in[0])
    scores = list(map(int, line_in[1:]))
    ave = sum(scores) / m
    print(ave)
    for j in scores:
        if ave < j:
            print(j)
            successes += 1
    percentage = str(successes / m)
    print(percentage)

