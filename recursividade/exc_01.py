def recursividade(base):
    if base == 0 or base == 1:
        return 1
    else:
        return 2 * recursividade(base - 1) - 4

print(recursividade(10))


