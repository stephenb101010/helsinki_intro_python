from string import ascii_uppercase

def initialize_variables(variables: dict):
    for letter in ascii_uppercase:
        variables[letter] = 0

def determine_value(input: str, variables: dict) -> int:
    if input in ascii_uppercase:
        return variables[input]
    else:
        return int(input)

def run(program: list):
    print_list = []
    variables = {}
    initialize_variables(variables)

    locations = []
    for index, command in enumerate(program):
        if ":" in command:
            location = command[:-1]
            locations.append((location, index))

    i = 0
    while i < len(program):
        ins = program[i]
        parts = ins.split(" ")
        action = parts[0]
        if action == "PRINT":
            to_print = parts[1]
            to_print = determine_value(to_print, variables)
            print_list.append(to_print)
        elif action == "MOV":
            var = parts[1]
            to_move = parts[2]
            to_move = determine_value(to_move, variables)
            variables[var] = to_move
        elif action == "ADD":
            var = parts[1]
            to_add = parts[2]
            to_add = determine_value(to_add, variables)
            variables[var] += to_add
        elif action == "SUB":
            var = parts[1]
            to_sub = parts[2]
            to_sub = determine_value(to_sub, variables)
            variables[var] -= to_sub
        elif action == "MUL":
            var = parts[1]
            to_mul = parts[2]
            to_mul = determine_value(to_mul, variables)
            variables[var] *= to_mul
        elif action == "JUMP":
            jump_to = parts[1]
            for loc in locations:
                if loc[0] == jump_to:
                    i = loc[1]
        elif action == "IF":
            first = parts[1]
            first = str(determine_value(first, variables))
            operator = parts[2]
            second = parts[3]
            second = str(determine_value(second, variables))
            result = eval(first + operator + second)
            if result:
                jump_to = parts[5]
                for loc in locations:
                    if loc[0] == jump_to:
                        i = loc[1]
        elif action == "END":
            return print_list

        i += 1
    return print_list

"""
def value(x, data):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if x in characters:
        return data[characters.index(x)]
    else:
        return int(x)

def condition(a, condition, b):
    if condition == "==":
        return a == b
    if condition == "!=":
        return a != b
    if condition == "<":
        return a < b
    if condition == "<=":
        return a <= b
    if condition == ">":
        return a > b
    if condition == ">=":
        return a >= b

def run(program):
    length = len(program)
    row = 0
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    data = [0]*26
    result = []
    while True:
        if row == length:
            break
        parts = program[row].split(" ")
        if parts[0] == "PRINT":
            result.append(value(parts[1], data))
        if parts[0] == "MOV":
            data[characters.index(parts[1])] = value(parts[2], data)
        if parts[0] == "ADD":
            data[characters.index(parts[1])] += value(parts[2], data)
        if parts[0] == "SUB":
            data[characters.index(parts[1])] -= value(parts[2], data)
        if parts[0] == "MUL":
            data[characters.index(parts[1])] *= value(parts[2], data)
        if parts[0] == "JUMP":
            row = program.index(parts[1]+":")
            continue
        if parts[0] == "IF":
            if condition(value(parts[1], data), parts[2], value(parts[3], data)):
                row = program.index(parts[5]+":")
                continue
        if parts[0] == "END":
            break
        row += 1
    return result
    """