curr = int(input())
correct = int(input())

if abs(curr - correct) == 180:
    print(180)
else:
    max_dir = 360 + min(correct, curr)
    change1 = max_dir - max(correct, curr) if curr > correct else -max_dir + max(correct, curr)
    change2 = correct - curr
    if abs(change1) < abs(change2):
        print(change1)
    else:
        print(change2)
