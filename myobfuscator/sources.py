import random


def get_neutral_sum(some_vars: list):
    if len(some_vars) == 1:
        x = some_vars[0] + ' + 1.5'
    else:
        x = ''
        random.shuffle(some_vars)
        for var in some_vars:
            x += f'{var} {random.choice(("+", "-"))} '
        x += '1.1'

    parts = [f'cos(2 * ({x}))', f'2 * pow(sin({x}), 2)',
             f'(- 2 * sin({x}) * cos({x}) / sin(2 * ({x})))']
    random.shuffle(parts)
    expr = ' + '.join(parts)

    return expr


def get_neutral_mul(some_vars: list):
    expr = 'pow(('

    for i in range(len(some_vars) - 1):
        operation = random.choice(("&", "|"))
        num = f'0x{random.randint(10, 255):X}'
        expr += f'(({some_vars[i]} * {num}) << {len(some_vars) - i}) {operation} '

    expr += f'(({some_vars[-1]} * 0xad) << 6)) + 5.5, {get_neutral_sum(some_vars)})'
    return expr


def get_sum(known: dict, start_index: int):
    if len(known) == 1:
        return str(random.choice(tuple(known.items())[0]))

    vars_sum = sum(tuple(known.values())[start_index::2])
    str_sum = ' + '.join(tuple(known.keys())[(start_index + 1) % 2::2])

    return str_sum + f' + {vars_sum}'


def obfuscator(value: int, known: dict, unknown: list):
    if type(value) is not int or type(known) is not dict or type(unknown) is not list:
        raise TypeError

    if len(known) == 0 or len(unknown) == 0:
        raise ValueError("List of variables can't be empty.")

    if not set(known.keys()).isdisjoint(set(unknown)):
        raise ValueError("Known and unknown vars cab't have common elements.")

    if len(unknown) == 1:
        tangle1 = get_neutral_sum(unknown)
        tangle2 = get_neutral_mul(unknown)
    else:
        mid = len(unknown) // 2
        tangle1 = get_neutral_sum(unknown[:mid])
        tangle2 = get_neutral_mul(unknown[mid:])

    if value == 0:
        return f'pow({tangle1} / {tangle2}, {random.randint(1, 1000)})'

    part1_1 = f'{get_sum(known, 0)}'
    part1_2 = f'( - ({tangle1}))'
    part1 = [part1_1, part1_2]
    random.shuffle(part1)
    part1 = ' + '.join(part1)

    num = value * random.randint(2, 10)
    part2 = f'{num} * ({tangle2} / {num / value} - ({get_sum(known, 1)}) / {float(num)})'

    parts = [part1, part2]
    random.shuffle(parts)
    obfuscated_expr = ' + '.join(parts)

    return obfuscated_expr
