def packet_starter_index(line, packet_size):
    for i in range(len(line)):
        if i>packet_size-1:
            shard = line[i-packet_size:i]
            if len(shard) == len(set(shard)):
                return i

def first_part(file):
    for line in file.readlines():
        return packet_starter_index(line, 4)

def second_part(file):
    for line in file.readlines():
        return packet_starter_index(line, 14)

def main():
    with open('day6\input.txt', 'r') as file:
        print(first_part(file))
    with open('day6\input.txt', 'r') as file:
        print(second_part(file))


if __name__ == "__main__":
    test = [
        'mjqjpqmgbljsphdztnvjfqwrcgsmlb', # expected = 7
        'bvwbjplbgvbhsrlpgdmjqwftvncz', # expected = 5
        'nppdvjthqldpwncqszvftbrmjlhg', # expected = 6
        'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', # expected = 10
        'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw' # expected = 11
    ]

    # print(f"for packet_size = 4: {[packet_starter_index(t, 4) for t in test]}")
    # print(f"for packet_size = 14: {[packet_starter_index(t, 14) for t in test]}")

    main()