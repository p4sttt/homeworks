def first(s, p):
    if s > 64 and p == 2:
        return True
    if p > 2:
        return False
    p += 1
    return first(s + 1, p) or first(s + 2, p) or first(s * 3, p)


for s in range(1, 65):
    if first(s, 0):
        print(s)  # 8
        break


def second(s, p):
    if s > 64 and (p == 1 or p % 2 == 0):
        return False
    if s > 64 and p == 3:
        return True
    if p > 3:
        return False
    p += 1
    if p % 2 == 0:
        return second(s + 1, p) and second(s + 2, p) and second(s * 3, p)
    else:
        return second(s + 1, p) or second(s + 2, p) or second(s * 3, p)


for s in range(1, 65):
    if second(s, 0):
        print(s)  # 7 19 20


def third(s, p):
    if s > 64 and p == 4:
        return True
    if (s > 64 and p == 1) or p > 4:
        return False
    p += 1
    if p % 2 == 0:
        return third(s + 1, p) or third(s + 2, p) or third(s * 3, p)
    else:
        return third(s + 1, p) and third(s + 2, p) and third(s * 3, p)


for s in range(1, 65):
    if third(s, 0):
        print(s)  # 6
        break
