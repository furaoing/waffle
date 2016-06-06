def expand_element(x, y, depth):
    code = []
    ax = x[depth]
    for i in ax:
        code.append(y + [i])
    return code


def expand_group(x, y, depth):
    code = []
    for a_list in y:
        code = code + expand_element(x, a_list, depth)
    return code


def helper(depth, bank):
    if depth == 0:
        tmp = bank[depth]
        ax = []
        for x in tmp:
            ax.append([x])
        return ax
    else:
        expanded = helper(depth-1, bank)
        return expand_group(bank, expanded, depth)


def generate_comb(bank):
    for i in range(len(bank)):
        if len(bank[i]) == 0:
            bank[i] = [None]
    if len(bank) > 1:
        width = len(bank)
        depth = width - 1
        result = helper(depth, bank)
        return result
    else:
        return bank


if __name__ == "__main__":
    bank = [['a', 'b'], [], ["k", "j"]]
    result = generate_comb(bank)
    print(result)
