from ctypes import Array


text_file = "day5/day5.txt"
part_1 = 0
part_2 = 0

def sort_fresh_ranges(fresh_ranges):
    return sorted(fresh_ranges, key=lambda x: x[0])

def enlarge_same_fresh_ranges(fresh_ranges):
    enlarged_fresh_ranges = []
    fresh_ranges = sort_fresh_ranges(fresh_ranges)
    while len(fresh_ranges) > 0:
        current_fresh_range = fresh_ranges.pop(0)
        i = 0
        while i < len(fresh_ranges):
            fresh_range = fresh_ranges[i]
            if current_fresh_range[0] == fresh_range[0] and fresh_range[1] > current_fresh_range[1]:
                current_fresh_range = (current_fresh_range[0], fresh_range[1])
                fresh_ranges.remove(fresh_range)
            else :
                i += 1
        enlarged_fresh_ranges.append(current_fresh_range)
    return enlarged_fresh_ranges

def enlarge_adjacent_fresh_ranges(fresh_ranges):
    enlarged_fresh_ranges = enlarge_same_fresh_ranges(fresh_ranges)
    enlarged_adjacent_fresh_ranges = []
    while len(enlarged_fresh_ranges) > 0:
        current_fresh_range = enlarged_fresh_ranges.pop(0)
        i = 0
        while i < len(enlarged_fresh_ranges):
            fresh_range = enlarged_fresh_ranges[i]
            if fresh_range[0] <= current_fresh_range[1] <= fresh_range[1]:
                current_fresh_range = (current_fresh_range[0], fresh_range[1])
                enlarged_fresh_ranges.remove(fresh_range)
            else :
                i += 1
        enlarged_adjacent_fresh_ranges.append(current_fresh_range)
    
    # remove inner ranges
    for fresh_range in enlarged_adjacent_fresh_ranges:
        for inner_fresh_range in enlarged_adjacent_fresh_ranges:
            if (fresh_range[0] < inner_fresh_range[0] and fresh_range[1] >= inner_fresh_range[1]) or (fresh_range[0] <= inner_fresh_range[0] and fresh_range[1] > inner_fresh_range[1]):
                enlarged_adjacent_fresh_ranges.remove(inner_fresh_range)
                break
    return enlarged_adjacent_fresh_ranges

def count_fresh_ranges(fresh_ranges):
    return sum([end - start + 1 for start, end in fresh_ranges])

with open(text_file) as f:
    fresh_ranges, ids = f.read().split("\n\n")
    fresh_ranges = fresh_ranges.split("\n")
    fresh_ranges = [(int(start), int(end)) for x in fresh_ranges for start, end in [x.split("-")]]
    ids = [int(x) for x in ids.split("\n")]
    for id in ids:
        for start, end in fresh_ranges:
            if id >= start and id <= end:
                part_1 += 1
                break
    
    enlarged_fresh_ranges = enlarge_adjacent_fresh_ranges(fresh_ranges)
    part_2 = count_fresh_ranges(enlarged_fresh_ranges)

print(part_1, part_2)