from itertools import combinations
from pprint import pprint


with open("input09.txt") as f:
    lines = [x.strip() for x in f.readlines()]

sample = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""".split("\n")

#lines = sample

points = []
for line in lines:
    x, y = line.split(",")
    points.append((int(x), int(y)))

p = points[0]
edges = [(points[-1][0], points[-1][1], p[0], p[1])]
for x2, y2 in points[1:]:
    x1, y1 = p
    edges.append((x1, y1, x2, y2))
    p = (x2, y2)

areas = []
for p1, p2 in combinations(points, 2):
    x1, y1 = p1
    x2, y2 = p2
    dx = abs(x2-x1)+1
    dy = abs(y2-y1)+1
    areas.append(dx*dy)

print(max(areas))

areas = []
for i, j in combinations(range(len(points)), 2):
    p1 = points[i]
    p2 = points[j]
    x1, y1 = p1
    x2, y2 = p2
    dx = abs(x2-x1)+1
    dy = abs(y2-y1)+1
    edge = None
    xmin = min(x1, x2)
    xmax = max(x1, x2)
    ymin = min(y1, y2)
    ymax = max(y1, y2)
    edge = False
    for k in range(len(points)):
        t = (k+1)%len(points)
        if k == i or k == j or t == i or t == j: continue
        e1 = points[k]
        e2 = points[(k+1)%len(points)]
        if (e1[0]<xmin and e2[0]<xmin) or (e1[0]>xmax and e2[0]>xmax):
            continue
        if (e1[1]<ymin and e2[1]<ymin) or (e1[1]>ymax and e2[1]>ymax):
            continue

        if e1[0]==xmin and e2[0]<xmin: continue
        if e2[0]==xmin and e1[0]<xmin: continue
        if e1[0]==xmax and e2[0]>xmax: continue
        if e2[0]==xmax and e1[0]>xmax: continue

        if e1[1]==ymin and e2[1]<ymin: continue
        if e2[1]==ymin and e1[1]<ymin: continue
        if e1[1]==ymax and e2[1]>ymax: continue
        if e2[1]==ymax and e1[1]>ymax: continue
        edge = True
        break

    if not edge:
        areas.append(dx*dy)

print(max(areas))
