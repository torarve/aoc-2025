with open("input05.txt") as f:
    lines = [x.strip() for x in f.readlines()]

sample = """3-5
10-14
16-20
12-18

1
5
8
11
17
32""".split("\n")

#lines = sample

ingredients: list[int] = []
ranges: list[tuple[int,int]] = []
tmp = False
for line in lines:
    if line == "":
        tmp = True
        continue
    if not tmp:
        x, y = tuple(int(z) for z in line.split("-"))
        ranges.append((x,y))
    else:
        ingredients.append(int(line))

count = 0
for i in ingredients:
    for a, b in ranges:
        if a <= i and i <= b:
            count += 1
            break

print(count)


done = False
while not done:
    new_ranges: list[tuple[int,int]] = []
    for start, end in ranges:
        overlap = False
        for i, (nstart, nend) in enumerate(new_ranges):
            if not (end<nstart or nend<start):
                new_ranges[i] = (min(start, nstart), max(end,nend))
                overlap = True
        
        if not overlap:
            new_ranges.append((start, end))

    done = len(new_ranges)==len(ranges)
    ranges = new_ranges

count = 0
for start, end in new_ranges:
    count += (end-start+1)

print(count)
