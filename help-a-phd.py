inp = int(input())

for i in range(inp):
    line_in = input()
    if line_in != "P=NP":
        a, b = map(int, line_in.split('+'))
        print(a+b)
    else:
        print("skipped")
