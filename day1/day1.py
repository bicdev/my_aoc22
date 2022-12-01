def main():
    data = {}
    with open('day1\input.txt', 'r') as file:
        elf_index = 0
        for line in file.readlines():
            if line == '\n':
                elf_index += 1
            else:
                if elf_index not in data.keys():
                    data[elf_index] = []
                clean = int(line.split('\n')[0])
                data[elf_index].append(clean)
    
    sum_to_elf = {}
    for elf, items in data.items():
        sum_to_elf[sum(items)] = elf
    
    sorted_biggest = sorted(sum_to_elf.keys(), reverse=True)
    
    biggest_sum = sorted_biggest[0]
    elf_with_biggest = sum_to_elf[biggest_sum]

    biggest_three = sorted_biggest[:3]
    biggest_three_sum = sum(biggest_three)

    print(biggest_three_sum)

if __name__ == "__main__":
    main()