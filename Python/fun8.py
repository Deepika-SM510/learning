def second_largest(a, b, c):
    if a > b and a > c:
        if b > c:
            return b
        else:
            return c

    elif b > a and b > c:
        if a > c:
            return a
        else:
            return c

    else:
        if a > b:
            return a
        else:
            return b


print(second_largest(10, 25, 15))