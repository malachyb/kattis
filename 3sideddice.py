inp = input().split()

while inp != ['0', '0', '0']:
    die_a = 0
    die_b = 0
    die_c = 0
    for i in range(3):
        die_a += int(inp[0])
        die_b += int(inp[1])
        die_c += int(inp[2])
        inp = input().split()
    reqs = list(map(int, inp))
    available = [die_a, die_b, die_c]
    cool = True
    for i in range(len(reqs)):
        if reqs[i] > available[i]:
            cool = False
    if cool:
        print("YES")
    else:
        print("NO")
    input()
    inp = input().split()
