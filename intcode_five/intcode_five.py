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
    if op in [1, 2, 7, 8]:
        return 4
    if op in [3, 4]:
        return 2
    if op in [5, 6]:
        return 3
    else:
        raise Exception("Cannot determine IP size: Invalid op code!")


def get_param_value(program: list, instruction: list, modes, index) -> list:

    param = instruction[index + 1]
    mode = parse_param_mode(modes, index)

    return param if mode == 1 else program[param]

def intcode(acc: list, ip: int, *args) -> list:
    read_param = 1 if len(args) == 0 else args[0]
    # print("\nacc: {}\nindex: {}".format(acc, index))
    (op, param_modes) = parse_op(acc[ip])

    if op == 99:
        return acc
    else:
        instruction = acc[ip:ip + ip_size(op)]
        if op not in [1, 2, 3, 4, 5, 6, 7, 8, 99]:
            raise Exception("Invalid op-code!")
        else:
            if op == 1:
                acc[instruction[-1]] = get_param_value(acc, instruction, param_modes, 0) + get_param_value(acc, instruction, param_modes, 1)
            elif op == 2:
                acc[instruction[-1]] = get_param_value(acc, instruction, param_modes, 0) * get_param_value(acc, instruction, param_modes, 1)
            elif op == 3:
                # read_string = input('')
                acc[instruction[-1]] = 1 if read_param is None else read_param
            elif op == 4:
                print(get_param_value(acc, instruction, param_modes, 0))
            elif op == 5:
                if get_param_value(acc, instruction, param_modes, 0) != 0:
                    # print(f'jump(6.1 is non-zero) to {get_param_value(acc, instruction, param_modes, 1)}')
                    return intcode(acc, get_param_value(acc, instruction, param_modes, 1))
            elif op == 6:
                # print(instruction)
                if get_param_value(acc, instruction, param_modes, 0) == 0:
                    # print(f'jump(6.1 is zero) to {get_param_value(acc, instruction, param_modes, 1)}')
                    return intcode(acc, get_param_value(acc, instruction, param_modes, 1))
            elif op == 7:
                acc[instruction[-1]] = 1 if get_param_value(acc, instruction, param_modes, 0) < get_param_value(acc, instruction, param_modes, 1) else 0
            elif op == 8:
                acc[instruction[-1]] = 1 if get_param_value(acc, instruction, param_modes, 0) == get_param_value(acc, instruction, param_modes, 1) else 0
            return intcode(acc, ip + ip_size(op))


def init_program(program, noun, verb):
    initialized = [program[0], noun, verb]
    initialized.extend(program[3:])
    return initialized

# intcode([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9],0, 2)