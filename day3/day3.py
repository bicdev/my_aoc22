def translate(s):
    if s.islower():
        return ord(s)-96
    else:
        return ord(s)-65+27

def common(a,b,c):
    return set(a).intersection(set(b)).intersection(set(c))

def first_part(file):
    total = 0
    for line in file.readlines(): # sample load
        line = line.strip('\n')

        half = len(line)//2
        
        first  = line[:half]
        second = line[half:]

        repeated = set(first) ^ (set(first) - set(second)) # genious O(1) repetition check
        r = repeated.pop()
        t = translate(r)
        total += t
    return total

def second_part(file):
    total = 0
    l = {}
    i = 0
    for line in file.readlines():
        line = line.strip('\n')

        j = i // 3
        i += 1

        if j not in l:
            l[j] = []
        l[j].append(line)

    for piece in l.values():
        r = common(*piece).pop()
        t = translate(r)
        total += t
    return total

def main():
    with open('day3\input.txt', 'r') as file:
        print(first_part(file))
        print(second_part(file))


if __name__ == "__main__":
    main()