inp = list(input().lower())
per = "per"
total = 0
for i in range(len(inp)):
    if inp[i] != per[i % len(per)]:
        total += 1
print(total)
