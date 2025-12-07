import functools


with open("input07.txt") as f:
    lines = [x.strip() for x in f.readlines()]

sample = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............""".split("\n")

# lines = sample

w = len(lines[0])
h = len(lines)
data = [x for x in "".join(lines)]

start = data.index("S")
beams = [start%w]

splits = 0
for y in range(1, h):
    new_beams = []
    for b in beams:
        if data[y*w + b] == "^":
            splits += 1
            new_beams.extend([b-1, b+1])
        else:
            new_beams.append(b)
    beams = [x for x in set(new_beams)]

print(splits)


@functools.cache
def timelines_from(x, y) -> int:
    if y == h: return 1
    if data[y*w+x] == "^":
        return timelines_from(x-1, y+1) + timelines_from(x+1, y+1)
    else:
        return timelines_from(x, y+1)


print(timelines_from(start%w, 1))