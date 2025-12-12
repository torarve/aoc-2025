with open("input12.txt") as f:
    lines = [x.strip() for x in f.readlines()]

sample = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2""".split("\n")

# lines = sample

shapes: list[str] = []
for i in range(5):
    tmps = lines[i*5+1]+lines[i*5+2]+lines[i*5+3]
    shapes.append(tmps)
    
block_count = tuple(x.count("#") for x in shapes)
count = 0
for line in lines[30:]:
    i = line.index(":")
    w, h = [int(x) for x in line[:i].split("x")]
    requirements = tuple(int(x) for x in line[i+1:].strip().split(" ") )
    if (w//3) * (h//3) >= sum(requirements):
        count += 1

print(count)
