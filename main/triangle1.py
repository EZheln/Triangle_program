def def_small_test(a, b, c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
    except ValueError:
        print("4")
        exit()

    if a <= 0 or b <= 0 or c <= 0:
        return 4
        exit()
    elif a != b and a != c and b != c:
        return 1
    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        return 2
    elif a == b and a == c and b == c:
        return 3
