def kelly(p, b):
    if b <= 0:
        return 0
    return max((p*(b+1)-1)/b, 0)
