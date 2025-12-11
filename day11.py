import functools


with open("input11.txt") as f:
    lines = [x.strip() for x in f.readlines()]

sample = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out""".split("\n")

sample2 = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out""".split("\n")

# lines = sample
# lines = sample2

connections: dict[str,list[str]] = {}
for line in lines:
    i = line.index(":")
    name = line[:i]
    connected_to = line[i+1:].strip().split(" ")
    connections[name] = connected_to

if "you" in connections.keys():
    current = connections["you"]
    count = 0
    while len(current)>0:
        next_step = []
        for name in current:
            if name == "out":
                count += 1
            else:
                try:
                    next_step.extend(connections[name])
                except:
                    pass
        current = next_step

    print(count)


@functools.cache
def counts(start: str, end: str):
    if start not in connections.keys():
        return 0
    
    if end in connections[start]:
        return 1
    
    return sum(counts(x, end) for x in connections[start])

if "svr" in connections.keys():
    res1 = counts("svr", "dac")*counts("dac", "fft")*counts("fft", "out")
    res2 = counts("svr", "fft")*counts("fft", "dac")*counts("dac", "out")
    print(res1+res2)