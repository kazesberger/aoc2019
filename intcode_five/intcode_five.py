def read_program(file):
    with open(file) as f:
        # read_data = map(int, f.read().split(","))
        read_data = f.read().split(",")

    return list(map(int, read_data))

def parse_op(num2parse: int):
    return (num2parse % 100, num2parse // 100)


def parse_param_mode(modes: int, index):
    return modes % (10**(index+1)) // 10**index


def ip_size(op: int) -> int:
    if op == 99:
        return 1
    if op in [1, 2]:
        return 4
    if op in [3, 4]:
        return 2

def get_param_value(program: list, instruction: list, modes, index) -> list:

    param = instruction[index + 1]
    mode = parse_param_mode(modes, index)

    return param if mode == 1 else program[param]


def intcode(acc: list, ip: int) -> list:
    # print("\nacc: {}\nindex: {}".format(acc, index))
    (op, param_modes) = parse_op(acc[ip])

    if op == 99:
        return acc
    else:
        instruction = acc[ip:ip + ip_size(op)]
        # print("command: {}".format(command))
        if op not in [1, 2, 3, 4]:
            raise Exception("Invalid operation!")
        else:
            if op == 1:
                acc[instruction[-1]] = get_param_value(acc, instruction, param_modes, 0) + get_param_value(acc, instruction, param_modes, 1)
            elif op == 2:
                acc[instruction[-1]] = get_param_value(acc, instruction, param_modes, 0) * get_param_value(acc, instruction, param_modes, 1)
            elif op == 3:
                # read_string = input('')
                read_string = "1"
                acc[instruction[-1]] = int(read_string)
            elif op == 4:
                print(get_param_value(acc, instruction, param_modes, 0))
            return intcode(acc, ip + ip_size(op))


def init_program(program, noun, verb):
    initialized = [program[0], noun, verb]
    initialized.extend(program[3:])
    return initialized
