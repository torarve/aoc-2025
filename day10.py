from scipy.optimize import linprog

with open("input10.txt") as f:
    lines: list[str] = [x.strip() for x in f.readlines()]

sample: list[str] = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}""".split("\n")

# lines = sample

def parse_wiring(s: str) -> tuple[int, ...]:
    return tuple(int(x) for x in s[1:-1].split(","))

def part1(schematic: str, buttons: list[tuple[int]]):
    seen: set[str] = set()
    current = ["." * len(schematic)]
    steps = 1
    while len(current)>0:
        next_set = []
        for c in current:
            for b in buttons:
                tmp = [x for x in c]
                for i in b:
                    tmp[i] = "#" if tmp[i] == "." else "."
                tmp2 = "".join(tmp)
                if tmp2 == schematic:
                    return steps
                elif tmp2 not in seen:
                    seen.add(tmp2)
                    next_set.append(tmp2)
        current = next_set
        steps += 1


def part2(buttons, requirements):
    r = tuple(int(x) for x in requirements.split(","))
    b_jolts = [tuple(1 if x in b else 0 for x in range(len(r))) for b in buttons]
    s = linprog(
        [1]*len(buttons),
        A_eq=[list(t) for t in zip(*b_jolts)],
        b_eq=list(r),
        bounds=[(0, None)]*len(buttons),
        integrality=[1]*len(buttons)
    )
    
    return s.fun


res1 = 0
res2 = 0
for line in lines:
    i = line.index("]")
    schematic = line[1:i]
    j = line.index("{")
    requirements = line[j+1:-1]
    buttons = [parse_wiring(x) for x in line[i+2:j-1].split(" ")]
    res1 += part1(schematic, buttons)
    res2 += part2(buttons, requirements)

print(res1)
print(res2)
