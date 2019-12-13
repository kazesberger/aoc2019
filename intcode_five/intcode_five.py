with open('02/input.txt') as f:
    # read_data = map(int, f.read().split(","))
    read_data = f.read().split(",")

program = list(map(int, read_data))


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

# def get_param(instruction: list, modes, index) -> list:


def intcode(acc: list, ip: int) -> list:
    # print("\nacc: {}\nindex: {}".format(acc, index))
    (op, param_modes) = parse_op(acc[ip])

    if op == 99:
        return acc
    else:
        instruction = acc[ip:ip + ip_size(op)]
        # print("command: {}".format(command))
        if op not in [1, 2]:
            raise Exception("Invalid operation!")
        else:
            if op == 1:
                acc[instruction[3]] = acc[instruction[1]] + acc[instruction[2]]
            else:
                acc[instruction[3]] = acc[instruction[1]] * acc[instruction[2]]
            return intcode(acc, ip + ip_size(op))


def init_program(program, noun, verb):
    initialized = [program[0], noun, verb]
    initialized.extend(program[3:])
    return initialized
