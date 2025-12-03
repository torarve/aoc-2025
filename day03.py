with open("input03.txt") as f:
    lines = [x.strip() for x in f.readlines()]

sample = """987654321111111
811111111111119
234234234234278
818181911112111""".split("\n")


def max_jolt(l: str, digits: int = 12) -> int:
    bank = [int(x) for x in l]
    r = digits
    res = 0
    i = -1
    while r > 1:
        a = max(bank[:-(r-1)])
        i = bank.index(a)
        bank = bank[i+1:]
        r -= 1
        res = res*10 + a

    res = res*10 + max(bank)
    return res


#lines = sample

t = [max_jolt(x, 2) for x in lines]
print(sum(t))
t2 = [max_jolt(x, 12) for x in lines]
print(sum(t2))
