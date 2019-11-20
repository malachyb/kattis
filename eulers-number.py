n = int(input())
e = 1
fact = 1

for i in range(n):
    fact *= i + 1
    e += 1/fact

print(e)
