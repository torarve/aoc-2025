import re

with open("input06.txt") as f:
    lines = [x.strip() for x in f.readlines()]

sample = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """.split("\n")

#lines = sample

def mul(a, b):
    return a*b
def add(a, b):
    return a+b
ops = [mul if x =="*" else add for x in re.split(r" +", lines[-1].strip())]


rows = []
for line in lines[:-1]:
    rows.append([int(x) for x in re.split(r" +", line.strip())])

res = list(x for x in rows[0])
for row in rows[1:]:
    for i in range(len(row)):
        res[i] = ops[i](res[i], row[i])

print(sum(res))

i = 0
current = []
rows = []
while i<len(lines[0]):
    digits = [l[i] for l in lines[:-1]]
    if any(len(x.strip())>0 for x in digits):
        tmp = 0
        for d in digits:
            if d==" ": continue
            tmp = tmp*10 + int(d)
        current.append(tmp)
    else:
        rows.append(current)
        current = []
    i += 1

rows.append(current)

res = 0
for i, row in enumerate(rows):
    tmp = row[0]
    for d in row[1:]:
        tmp = ops[i](tmp, d)
    res += tmp

print(res)