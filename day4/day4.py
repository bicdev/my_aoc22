def first_part(file):
    total = 0

    for line in file.readlines():
        a, b = line.strip('\n').split(',')

        a_start, a_end = a.split('-')
        b_start, b_end = b.split('-')

        a_start, a_end = int(a_start), int(a_end)
        b_start, b_end = int(b_start), int(b_end)

        if (a_start <= b_start) and (a_end >= b_end):
            print(f'{a_start}-{a_end} contains {b_start}-{b_end} --> {(a_start <= b_start)} and {(a_end >= b_end)}')
            total += 1 # descending piramid
        elif (a_start >= b_start) and (a_end <= b_end):
            print(f'{a_start}-{a_end} is contained by {b_start}-{b_end}')
            total += 1 # ascending piramid

    return total

def second_part(file):
    total = 0
    
    for line in file.readlines():
        a, b = line.strip('\n').split(',')

        a_start, a_end = a.split('-')
        b_start, b_end = b.split('-')

        a_start, a_end = int(a_start), int(a_end)
        b_start, b_end = int(b_start), int(b_end)

        a_range = set(range(a_start, a_end+1))
        b_range = set(range(b_start, b_end+1))

        if a_range.intersection(b_range):
            total += 1

    return total

def main():
    with open('day4\input.txt', 'r') as file:
        # print(first_part(file))
        print(second_part(file))


if __name__ == "__main__":
    main()