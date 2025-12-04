text_file = "day4/day4.txt"
part_1 = 0
part_2 = 0
index_offset_to_check = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]]

def is_accessible(lines, x, y):
    neighbors_count = 0
    for offset in index_offset_to_check:
        if offset == (0, 0):
            continue
        y_to_check = y + offset[1]
        x_to_check = x + offset[0]
        if y_to_check < 0 or y_to_check >= len(lines) or x_to_check < 0 or x_to_check >= len(lines[y_to_check]):
            continue
        if lines[y_to_check][x_to_check] == "@":
            neighbors_count += 1
    return neighbors_count < 4

def step(lines):
    new_lines = lines.copy()
    result = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "@":
                if is_accessible(lines, x, y):
                    result += 1
                    new_lines[y] = new_lines[y][:x] + "." + new_lines[y][x+1:]
    return (new_lines, result)

with open(text_file) as f:
    lines = [x.strip() for x in f.readlines()]
    new_lines, part_1 = step(lines)
    part_2 += part_1

    while new_lines != lines:
        lines = new_lines
        new_lines, result = step(lines)
        part_2 += result
    
print(part_1, part_2)