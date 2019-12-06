with open('input.txt') as f:
    # read_data = map(int, f.read().split(","))
    read_data = f.read().split(",")

# print(read_data)
program = list(map(int, read_data))
# print(list(/program))
print(program)

program[1] = 12
program[2] = 2

print(program)

def program1202(acc: list, index: int) -> list:
    print("\nacc: {}\nindex: {}".format(acc, index))
    if acc[index] == 99:
        return acc
    else:
        command = acc[index:index + 4]
        print("command: {}".format(command))
        if command[0] not in [1, 2]:
            raise Exception("Invalid operation!")
        else:

            acc[command[3]] = acc[command[1]] + acc[command[2]] if command[0] == 1 else acc[command[1]] * acc[command[2]]
            return program1202(acc, index + 4)


start_index = 0

print("result: %d" % (program1202(program, start_index)[0]))

# print("sample: {}".format(program1202([2, 4, 4, 5, 99, 0], start_index)))
# print("sample: % d" % (program1202([1, 1, 1, 4, 99, 5, 6, 0, 99], start_index)[0]))
