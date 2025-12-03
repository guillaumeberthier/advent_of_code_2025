text_file = "day2/day2.txt"
part_1 = 0
part_2 = 0

def is_invalid(id):
    prefix, suffix = id[len(id)//2:], id[:len(id)//2]
    if prefix == suffix:
        return 1
    return 0

def windows(id, size):
    if len(id) % size != 0:
        return []
    id_spans = [id[i:i+size] for i in range(0, len(id), size)]
    return id_spans

def is_invalid_2(id):
    for i in range(1, len(id)//2 + 1):
        w = windows(id, i)
        if len(w) > 0 and all([w[0] == x for x in w]):
            return 1
    return 0

with open(text_file) as f:
    lines = f.readlines()

for line in lines:
    ranges = line.split(",")
    for span in ranges:
        start, end = span.split("-")
        for id in range(int(start), int(end) + 1):
            part_1 += id * is_invalid(str(id))
            part_2 += id * is_invalid_2(str(id))

print(part_1, part_2)