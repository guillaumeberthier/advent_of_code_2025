text_file = "day3/day3.txt"
part_1 = 0
part_2 = 0

def max_joltage(line, joltage_size, current_joltage):
    if len(current_joltage) == joltage_size:
        return int(current_joltage)
    for v in range(9, -1, -1):
        range_to_check = range(len(line) - (joltage_size - len(current_joltage)) + 1)
        for i in range_to_check:
            if line[i] == str(v):
                return max_joltage(line[i+1:], joltage_size, current_joltage + str(v))
    raise Exception(f"No more joltage found for {line} with size {joltage_size} and current {current_joltage}")

with open(text_file) as f:
    lines = f.readlines()

for line in lines:
    joltage_1 = max_joltage(line.strip(), 2, "")
    part_1 += joltage_1
    joltage_2 = max_joltage(line.strip(), 12, "")
    part_2 += joltage_2

print(part_1, part_2)