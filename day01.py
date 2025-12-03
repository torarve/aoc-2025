
with open("input01.txt") as f:
    lines = [x.strip() for x in f.readlines()]

input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".split("\n")

#lines = input

current = 50
count = 0
count2 = 0
for l in lines:
    i = int(l[1:])
    prev = current
    if i > 100:
        count2 += i // 100
    if l[0]=="L":
        current -= i%100
        if prev != 0 and current < 0:
            count2 += 1
    if l[0]=="R":
        current += i%100
        if current > 100:
            count2 += 1

    current %= 100
    if current == 0:
        count2 += 1
        count += 1

print(count)
print(count2)