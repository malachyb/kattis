cases = int(input())

for i in range(cases):
    sounds = input().split()
    line_in = input()
    while line_in != "what does the fox say?":
        sound = line_in.split()[2]
        j = 0
        while j < len(sounds):
            if sounds[j] == sound:
                sounds.pop(j)
            else:
                j -= -1
        line_in = input()
    print(" ".join(sounds))
