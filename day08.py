with open("input08.txt") as f:
    lines = [x.strip() for x in f.readlines()]

sample = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689""".split("\n")

# lines = sample

points: list[tuple[int,int,int]] = []
for line in lines:
    x, y, z = line.split(",")
    points.append((int(x), int(y), int(z)))


def d(p1: tuple[int,int,int], p2: tuple[int, int, int]) -> int:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2

# print(points)
import itertools
from pprint import pprint

distances = []
for i, j in itertools.combinations(range(len(points)), 2):
    distances.append((d(points[i], points[j]), i, j))

distances.sort(key = lambda p: p[0])
circuits: list[set] = [set([x]) for x in range(len(points))]
count = 0
for i in range(len(distances)):
    d, i, j = distances[i]
    new_circuits: list[set] = []
    tmp1: set = None
    tmp2: set = None
    for circuit in circuits:
        if i in circuit and j in circuit:
            new_circuits.append(circuit)
        elif i in circuit:
            tmp1 = circuit
        elif j in circuit:
            tmp2 = circuit
        else:
            new_circuits.append(circuit)
        
    if tmp1 is not None and tmp2 is not None:
        new_circuits.append(tmp1.union(tmp2))

    if len(circuit)!=len(new_circuits):
        count += 1
    circuits = new_circuits
    if count == 1000:
        break

circuit_sizes = [len(x) for x in circuits]
circuit_sizes.sort(reverse=True)
# print(circuit_sizes)
a, b, c = tuple(circuit_sizes[:3])
print(a*b*c)
# pprint(distances[0:10])

circuits: list[set] = [set([x]) for x in range(len(points))]
for i in range(len(distances)):
    d, i, j = distances[i]
    new_circuits: list[set] = []
    tmp1: set = None
    tmp2: set = None
    for circuit in circuits:
        if i in circuit and j in circuit:
            new_circuits.append(circuit)
        elif i in circuit:
            tmp1 = circuit
        elif j in circuit:
            tmp2 = circuit
        else:
            new_circuits.append(circuit)
        
    if tmp1 is not None and tmp2 is not None:
        new_circuits.append(tmp1.union(tmp2))

    circuits = new_circuits
    if len(circuits) == 1:
        print(points[i][0] * points[j][0])
        break