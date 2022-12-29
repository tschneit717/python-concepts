x = [1, 2, 1231, 2, 94, 12, 3244, 992, 1231, 3322]

# take lambda func and apply it to all items in list
mp = map(lambda i: i / 2, x)

print(list(mp))

fl = filter(lambda i: i / 2 > 500, x)
print(list(fl))


def func(i):
    i = i * 3
    return i % 2 == 0


fl2 = filter(func, x)
print(list(fl2))
