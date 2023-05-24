import itertools


def f(n):
    n = bin(n)[2:]
    for _ in range(0, 2):
        n += str(n.count("1") % 2)
    return int(n, 2)


for n in range(0, 100):
    if f(n) > 150:
        print(f(n))  # 154
        break

c = 0
for i in itertools.permutations("КАПКАН"):
    i = ''.join(i)
    if "КК" in i or "АА" in i or "ПП" in i or "НН" in i:
        c += 1
print(c)  # 384

s = "111111111111111111111111111111111111111111111111112222222222222222222222222222222222222222222222222233333333333333333333333333333333333333333333333333"
while "12" in s or "32" in s or "31" in s:
    if "12" in s:
        s = s.replace("12", "21", 1)
    if "32" in s:
        s = s.replace("32", "23", 1)
    if "31" in s:
        s = s.replace("31", "13", 1)
print(s[19], s[79], s[119])  # 2 1 3

for a in range(200, 1000):
    fl = True
    for x in range(0, 100):
        if not ((not ((x % a == 0) and (x % 45 == 0)) or (x % 162 == 0)) and (a > 200)):
            fl = False
    if fl:
        print(a)  # 201
        break
