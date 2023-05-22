for a in range(0, 1000):
    f = True
    for x in range(0, 100):
        if not (not ((x % 12 == 0) or (not (x % 90 == 0))) or ((x + 2 * a) >= 512)):
            f = False
    if f:
        print(a)  # 256
        break

for a in range(0, 1000):
    f = True
    for x in range(0, 100):
        for y in range(0, 100):
            if not ((y - 2 * x < a) or (x > 15) or (y > 20)):
                f = False
    if f:
        print(a)  # 21
        break

for a in range(0, 1000):
    f = True
    for x in range(0, 100):
        for y in range(0, 100):
            if (x * y > a) and (x > y) and (x < 8):
                f = False
    if f:
        print(a)  # 42
        break

for a in range(1000, 0, -1):
    f = True
    for x in range(0, 100):
        for y in range(0, 100):
            if not (not ((x + y - 73) > 0) or not ((37 - x + y) > 0) or ((y - a) > 0)):
                f = False
    if f:
        print(a)  # 18
        break
