per = "per"
text = input().lower()
steps = 0

for i in range(len(text)):
    if text[i] != per[i % len(per)]:
        steps += 1

print(steps)
