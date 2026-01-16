tem = ""
a = 2
b = 3
x = 1

result = 0

while x <= b:

    if x != b:
        tem += str(a) + ("+")
    else:
        tem += str(a)
    result += a
    x += 1

tem += ("=") + str(result)
print(tem)