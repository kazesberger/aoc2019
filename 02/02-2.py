with open('input.txt') as f:
    # read_data = map(int, f.read().split(","))
    read_data = f.read().split(",")

# print(read_data)
program = list(map(int, read_data))
# print(list(/program))
print(program)


def intcode(acc: list, index: int) -> list:
    # print("\nacc: {}\nindex: {}".format(acc, index))
    if acc[index] == 99:
        return acc
    else:
        command = acc[index:index + 4]
        # print("command: {}".format(command))
        if command[0] not in [1, 2]:
            raise Exception("Invalid operation!")
        else:

            acc[command[3]] = acc[command[1]] + acc[command[2]] if command[0] == 1 else acc[command[1]] * acc[
                command[2]]
            return intcode(acc, index + 4)


def init_program(program, noun, verb):
    initialized = [program[0], noun, verb]
    initialized.extend(program[3:])
    return initialized


start_index = 0

input_options = set()

# for x in range(99):
#     for y in range(99):
#         input_options.add((x, y))

for x in range(99):
    for y in range(x, 99):
        input_options.add((x, y))




print(len(input_options))

print(f'input_options: {input_options}')

for input in input_options:
    foo = list(input)
    print(f'{input}')
    print(f'{foo[0]} : {foo[1]}')
    result = intcode(init_program(program, foo[0], foo[1]), start_index)[0]
    if result == 19690720:
        asdf = foo[0] * 100 + foo[1]
        print(f'result: {asdf}')
        break
