from itertools import combinations, combinations_with_replacement
from pprint import pprint


with open("input10.txt") as f:
    lines: list[str] = [x.strip() for x in f.readlines()]

sample: list[str] = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}""".split("\n")

# lines = sample

def parse_wiring(s: str) -> tuple[int]:
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

def _part2(schematic: str, buttons: list[tuple[int]], requirement: list[int]):
    # seen: set[tuple[str, tuple[int]]] = set()
    working_set = [("." * len(schematic), tuple([0]*len(requirement)), 0, 0)]
    steps = 1
    best = 0
    max_steps = sum(requirement)
    while len(working_set)>0:
        state, jolt, depth, b_i = working_set.pop()
        if b_i+1<len(buttons):
            working_set.append((state, jolt, depth, b_i+1))
        if depth==max_steps:
            continue
        b = buttons[b_i]
        # for b in sorted(buttons, key=lambda x: len(x),reverse=True):
        tmp = [x for x in state]
        tmp2 = list(jolt)
        for i in b:
            tmp[i] = "#" if tmp[i] == "." else "."
            tmp2[i] = tmp2[i] + 1
        tmp3 = "".join(tmp)
        if tmp3 == schematic and tuple(tmp2)==requirement:
            # Found solution
            return depth
        elif all(x<=y for x,y in zip(tmp2, requirement)):
            working_set.append((tmp3, tuple(tmp2), depth+1, 0))
            # next_set.append((tmp3, tuple(tmp2)))
        else:
            pass
 
def part2_work(i, times_button_can_be_pushed, b_jolts, r):
    if i>=len(times_button_can_be_pushed):
        return 0
    res = 0

    #upper_limit = 
    #times_button_can_be_pushed = []
    m = min(y for x,y in zip(b_jolts[i], r) if x == 1)
    # if m==0:
    #     return 0
    # times_button_can_be_pushed.append(m)
    # for times in range(times_button_can_be_pushed[i],-1,-1):
    for times in range(m,-1,-1):
        r2 = tuple(x-times*y for x,y in zip(r,b_jolts[i]))
        if all(x==0 for x in r2):
            print("  "*i, f"{i}: {times} times")
            return times
        if all(x>=0 for x in r2):
            n = part2_work(i+1, times_button_can_be_pushed, b_jolts, r2)
            if n > 0:
                print("  "*i, times,n)
                
                if res == 0 or res > times+n:
                    res = times+n
                # return times+n
    if res > 0:
        print(f">> {res}")
    return res

import sympy

def part2(buttons, requirements):
    print(">>>")
    r = tuple(int(x) for x in requirements.split(","))
    b_jolts = [tuple(1 if x in b else 0 for x in range(len(r))) for b in buttons]

    m = sympy.Matrix(b_jolts)
    x = sympy.symbols(" ".join(f"x{i}" for i in range(len(buttons))), positive=True)
    b = sympy.Matrix(r)
    s = sympy.linsolve([m, b], *x)
    return 0

    times_button_can_be_pushed = []
    for b in b_jolts:
        m = min(y for x,y in zip(b, r) if x == 1)
        times_button_can_be_pushed.append(m)
    m = min(r)
    i = r.index(m)

    res = 0
    for i in range(len(buttons)):
        t = part2_work(i, times_button_can_be_pushed, b_jolts, r)
        if t > 0 and (res==0 or t<res):
            print(f">{t}")
            res = t
        # for times in range(times_button_can_be_pushed[i],0,-1):
        #     r2 = tuple(x-times*y for x,y in zip(r,b_jolts[i]))
        #     print(r2)
        #break
    return res
    # print(m)
    #print(2**max(r), len(tmp))
    # pprint(tmp)
    #print(times_button_can_be_pushed)
    # print(m, [x for x in b_jolts if x[i]==1])
    # for times_button_can_be_pushed in range(max(r), sum(r)+1):
    #     print(times_button_can_be_pushed)
    #     for c in combinations(tmp, times_button_can_be_pushed):
    #         tmp2 = [0] * len(r)
    #         for j in c:
    #             for i in range(len(tmp2)):
    #                 tmp2[i] += j[i]
    #         # print(s, tmp)
    #         if tuple(tmp2) == r:
    #             # print(s)
    #             return times_button_can_be_pushed


res1 = 0
res2 = 0
for line in lines:
    i = line.index("]")
    # schematic = [True if x=="#" else False for x in line[1:i]]
    schematic = line[1:i]
    j = line.index("{")
    requirements = line[j+1:-1]
    # print(line[i+2:j-1].split(" "))
    buttons = [parse_wiring(x) for x in line[i+2:j-1].split(" ")]
    buttons.sort(key=lambda k: len(k), reverse=False)
    print(schematic, buttons) #, requirements)
    res1 += part1(schematic, buttons)
    # res2 += part2(schematic, buttons, tuple(int(x) for x in requirements.split(",")))
    res2 += part2(buttons, requirements)

print(res1)
print(res2)