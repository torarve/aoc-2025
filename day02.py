
with open("input02.txt") as f:
    lines = [x.strip() for x in f.readlines()]

sample = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124""".split("\n")

# lines = sample


def is_valid(id: int) -> bool:
    s = str(id)
    if len(s)%2 != 0: return True
    return s[:len(s)//2] != s[len(s)//2:]



def is_valid2(id: int) -> bool:
    s = str(id)
    split_into = 2
    while split_into<=len(s):
        if len(s)%split_into == 0:
            size = len(s)//split_into
            m = s[:size]
            is_valid = False
            for i in range(1, split_into):         
                if s[i*size:(i+1)*size] != m:
                    is_valid = True
            if not is_valid:
                return False

        split_into += 1

    return True

ranges = lines[0].split(",")
result = 0
result2 = 0
for r in ranges:
    start, end = tuple(int(x) for x in r.split("-"))
    for i in range(start, end+1):
        if not is_valid(i):
            result += i
        if not is_valid2(i):
            result2 += i

print(result)
print(result2)