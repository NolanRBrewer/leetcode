# merge triplets to form target triplet

triplets = [[3, 5, 1], [10, 5, 7]]
target = [3, 5, 7]


def merge_triplets(triplets: list[list[int]], target: list[int]) -> bool:
    match = []

    for triplet in triplets:
        if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
            continue
        for index, value in enumerate(triplet):
            if value == target[index]:
                match.append(value)
    return len(match) == len(set(target))


print(merge_triplets(triplets, target))
