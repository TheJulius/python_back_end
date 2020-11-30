def recursividade(base):
    if base == 0 or base == 1:
        return 1
    else:
        return base * recursividade(base - 1)

print(recursividade(10))


