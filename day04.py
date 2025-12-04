with open("input04.txt") as f:
    lines = [x.strip() for x in f.readlines()]

sample = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".split("\n")

# lines = sample

h = len(lines)
w = len(lines[0])
map = [x for x in "".join(lines)]


def is_roll(x, y) -> int:
    return 1 if map[x+y*w] != "." else 0


def adajacent_count(x, y):
    count = 0
    if is_roll(x,y) == 1:
        if x>0:
            count += is_roll(x-1, y)
            if y>0:
                count += is_roll(x-1, y-1)
            if y<h-1:
                count += is_roll(x-1, y+1)
        if x<w-1:
            count += is_roll(x+1, y)
            if y>0:
                count += is_roll(x+1, y-1)
            if y<h-1:
                count += is_roll(x+1, y+1)
        if y>0:
            count += is_roll(x, y-1)
        if y<h-1:
            count += is_roll(x, y+1)
    return count


def mark_rolls_that_can_be_removed():
    removed_count = 0
    for x in range(0, w):
        for y in range(0, h):
            if is_roll(x,y) and adajacent_count(x, y)<4:
                removed_count +=1
                map[x + y*w] = "x"

    return removed_count


result = mark_rolls_that_can_be_removed()
print(result)

removed = 0
step = mark_rolls_that_can_be_removed()
while step != 0:
    removed += step
    map = ["." if x == "x" else x for x in map]
    step = mark_rolls_that_can_be_removed()

print(removed)