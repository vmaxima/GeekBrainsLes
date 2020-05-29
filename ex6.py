a, b = int(input()), int(input())

x = 1
while a <= b:
    a += (a * 0.1)
    x += 1

print(x)
