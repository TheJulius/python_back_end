def recursividade(base):
    if base == 0 or base == 1:
        return 1
    else:
        return ((2 * (recursividade(base)*recursividade(base)))+(2 * recursividade(base)) + 8) (base - 1)

print(recursividade(2))
