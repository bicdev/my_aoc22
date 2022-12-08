def first_part(file):
    stack = {}
    instructions = []
    
    line_index = 1
    for line in file.readlines():
        line = line.strip('\n')
        if line_index < 9:
            stack = extract_line(stack, line)
        elif line_index == 9 or line_index == 10:
            pass
        else:
            instructions.append(line.split(' ')[1::2])
        line_index += 1
    
    for instruction in instructions:
        stack = apply_instruction(stack, instruction)        

    return extract_top_line(stack)

def second_part(file):
    stack = {}
    instructions = []
    
    line_index = 1
    for line in file.readlines():
        line = line.strip('\n')
        if line_index < 9:
            stack = extract_line(stack, line)
        elif line_index == 9 or line_index == 10:
            pass
        else:
            instructions.append(line.split(' ')[1::2])
        line_index += 1
    
    for instruction in instructions:
        stack = apply_instruction(stack, instruction, mode='multiple')        

    return extract_top_line(stack)

def extract_line(stack, line):
    chunk_size = 4
    chunked_line = [line[i:i+chunk_size] for i in range(0, len(line), chunk_size)]
    for crate in chunked_line:
        if crate != '    ':
            index = chunked_line.index(crate)+1
            if index in stack.keys():
                if crate in stack[index]:
                    temp_list = chunked_line.copy()
                    temp_list.remove(crate)
                    index = temp_list.index(crate)+2

        if len(crate) == 3:
            crate += " "

        if crate != '    ':
            if index not in stack.keys():
                stack[index] = []

            stack[index].append(crate)

    return stack

def apply_instruction(stack, instruction, mode='one by one'):
    amount, from_, to = [int(i) for i in instruction]

    if mode == 'one by one':
        for i in range(amount):
            stack[to].insert(0, stack[from_].pop(0)) # always remove from index 0 and insert into position 0, shifting..
    elif mode == 'multiple':
        slice_ = stack[from_][:amount]

        for e in slice_:
            stack[from_].remove(e)
        for e in slice_[::-1]:
            stack[to].insert(0, e)

    return stack

def extract_top_line(stack):
    top_line = ''
    
    from collections import OrderedDict

    for k,v in OrderedDict(sorted(stack.items())).items():
        top_line += v[0][1:2]
    return top_line

def main():
    with open('day5\input.txt', 'r') as file:
        # print(first_part(file))
        print(second_part(file))


if __name__ == "__main__":
    # stack = {
    #     1 : ['[N] ', '[Z] '],
    #     2 : ['[D] ', '[C] ', '[M] '],
    #     3 : ['[P] ']
    # }

    # d = [
    #     [1,2,1],
    #     [3,1,3],
    #     [2,2,1],
    #     [1,1,2]
    # ]

    # for i in d:
    #     print(apply_instruction(stack, i,  mode='multiple'))
    # print(extract_top_line(stack))
    
    main()