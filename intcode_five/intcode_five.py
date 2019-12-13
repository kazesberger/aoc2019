with open('02/input.txt') as f:
    # read_data = map(int, f.read().split(","))
    read_data = f.read().split(",")

program = list(map(int, read_data))


def parse_op(num2parse: int):
    return (num2parse % 100, num2parse // 100)


def ip_size(op: int) -> int:
    if op == 99:
        return 1
    if op in [1, 2]:
        return 4
    if op in [3, 4]:
        return 2


def intcode(acc: list, ip: int) -> list:
    # print("\nacc: {}\nindex: {}".format(acc, index))
    op = acc[ip]

    if op == 99:
        return acc
    else:
        instruction = acc[ip:ip + ip_size(op)]
        # print("command: {}".format(command))
        if op not in [1, 2]:
            raise Exception("Invalid operation!")
        else:
            acc[instruction[3]] = acc[instruction[1]] + acc[instruction[2]] if op == 1 else acc[instruction[1]] * acc[
                instruction[2]]
            return intcode(acc, ip + ip_size(op))


def init_program(program, noun, verb):
    initialized = [program[0], noun, verb]
    initialized.extend(program[3:])
    return initialized


list("asdf1234")[-2:]



start_index = 0

input_options = set()

# for x in range(99):
#     for y in range(99):
#         input_options.add((x, y))

for x in range(99):
    for y in range(99):
        input_options.add((x, y))

# print(len(input_options))

# print(f'input_options: {input_options}')

for i in input_options:
    option = list(i)
    # print(f'{input}')
    # print(f'{foo[0]} : {foo[1]}')
    result = intcode(init_program(program, option[0], option[1]), start_index)[0]
    if result == 19690720:
        solution = option[0] * 100 + option[1]
        print(f'result: {solution}')
        # break

